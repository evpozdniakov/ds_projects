import category_encoders as ce
import sys
import pandas as pd
from textblob import TextBlob
import time

DEBUG = '-d' in sys.argv

binary_encoders = None
def apply_binary(data, features):
    global binary_encoders

    if binary_encoders is None:
        binary_encoders = dict()

    for feature in features:
        # print(f'len(data[feature].unique()) = {len(data[feature].unique())}')
        if len(data[feature].unique()) > 2047:
            convert_rare_values_to_others(data, feature, how_many_to_keep=127)

        if binary_encoders.get(feature) is None:
            binary_encoders[feature] = ce.BinaryEncoder()
            binary_encoders[feature].fit(data[feature])

        encoded_feature = binary_encoders[feature].transform(data[feature])
        data[encoded_feature.columns] = encoded_feature

onehot_encoders = None
def apply_onehot(data, features):
    global onehot_encoders

    if onehot_encoders is None:
        onehot_encoders = dict()

    for feature in features:
        # print(f'"{feature}" unique values: {len(data[feature].unique())}')
        if len(data[feature].unique()) > 15:
            convert_rare_values_to_others(data, feature)
        
        if onehot_encoders.get(feature) is None:
            onehot_encoders[feature] = ce.OneHotEncoder()
            onehot_encoders[feature].fit(data[feature])

        encoded_feature = onehot_encoders[feature].transform(data[feature])
        data[encoded_feature.columns] = encoded_feature

def convert_rare_values_to_others(data, feature='', how_many_to_keep=15):
    value_counts = data[feature].value_counts()

    difference_times = value_counts[0] / value_counts[how_many_to_keep]

    if difference_times < 100:
        debug_print(f'!! convert_rare_values_to_others for "{feature}"')
        debug_print(f'value_counts: {len(value_counts)}')
        debug_print(f'value_counts[0]: {value_counts[0]}')
        debug_print(f'value_counts[{how_many_to_keep}]: {value_counts[how_many_to_keep]}')
        debug_print(f'difference is {difference_times} times')

    allowed_values = value_counts.index[0: how_many_to_keep]
    data[feature] = data[feature].apply(lambda x: x if x in allowed_values else '-- others --')

def count_words(text):
    return len([word for word in text.split(' ') if len(word) > 0])

def debug_print(*args, **kwargs):
    global DEBUG

    if DEBUG:
        print(*args, **kwargs)

concap = None
concap_dict = dict()
def get_city_lat_lng(city_name):
    global concap
    global concap_dict

    if concap is None:
        concap = pd.read_csv('concap.csv')

    if concap_dict.get(city_name) is None:
        m = concap['CapitalName'] == city_name

        if m.sum() != 1:
            raise ValueError(f'Unable to find "{city_name}" in concap')

        city = concap[m]

        concap_dict[city_name] = {
            'lat': float(city['CapitalLatitude'].values[0]),
            'lng': float(city['CapitalLongitude'].values[0]),
        }

    return concap_dict[city_name]

def get_polarity(text):
    return TextBlob(text).sentiment.polarity

def logger(fn):
    def decorated(*args, **kwargs):
        debug_print(f'>>> fn. `{fn.__name__}` is running')
        ts = time.time()
        res = fn(*args, **kwargs)
        te = time.time()
        delta = round((te-ts) * 1000)
        sec_mls = 'mls'
        if delta > 1000:
            delta = round(delta / 1000, 1)
            sec_mls = 's'
        debug_print(f'<<< fn. `{fn.__name__}` finished, took {delta} {sec_mls}\n')
        return res
    return decorated
