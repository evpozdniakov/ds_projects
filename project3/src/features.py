#!/Users/ev/opt/anaconda3/bin/python

from geopy import distance
import json
import pandas as pd

# local modules
from helpers import apply_binary
from helpers import apply_onehot
from helpers import count_words
from helpers import debug_print
from helpers import get_city_lat_lng
from helpers import get_polarity
from helpers import logger

@logger
def add_all(data):
    add_city(data)
    add_city_center_lat_lng(data)
    add_distance_to_city_center(data)
    # add_time_features(data)
    # add_review_polarity(data)
    # recount_review_words(data)
    # parse_days_since_review(data)
    # parse_tags(data)
    # apply_onehot(data, ['hotel_city', 'month', 'year'])
    # apply_binary(data, ['hotel_address', 'reviewer_nationality'])

@logger
def add_city(data):
    def get_city(addr):
        city_country = addr.split(' ')[-2:]
        if ' '.join(city_country) == 'United Kingdom':
            return 'London'
        return city_country[0]

    data.loc[:, 'hotel_city'] = data['hotel_address'].apply(get_city)
    debug_print(data['hotel_city'].value_counts())

@logger 
def add_city_center_lat_lng(data):
    def set_city_coords(row):
        city_coords = get_city_lat_lng(row['hotel_city'])
        row['city_center_lat'] = city_coords['lat']
        row['city_center_lng'] = city_coords['lng']
        return row

    data.loc[:, ['city_center_lat', 'city_center_lng']] = data.apply(set_city_coords, axis=1)

@logger
def add_distance_to_city_center(data):
    def get_distance(cols):
        coord_1 = (cols['city_center_lat'], cols['city_center_lng'])
        coord_2 = (cols['lat'], cols['lng'])
        return round(distance.distance(coord_1, coord_2).km, 1)

    data.loc[:, 'distance_to_city_center_km'] = data.apply(get_distance, axis=1)
    data.loc[:, 'is_center'] = data['distance_to_city_center_km'].apply(lambda x: 1 if x < 1.5 else 0)
    data.loc[:, 'is_walking_distance'] = data['distance_to_city_center_km'].apply(lambda x: 1 if x >= 1.5 and x < 3.0 else 0)
    data.loc[:, 'is_not_far'] = data['distance_to_city_center_km'].apply(lambda x: 1 if x >= 3.0 and x < 6.0 else 0)
    data.loc[:, 'is_far'] = data['distance_to_city_center_km'].apply(lambda x: 1 if x >= 6.0 and x < 12.0 else 0)
    data.loc[:, 'is_far_away'] = data['distance_to_city_center_km'].apply(lambda x: 1 if x > 12.0 else 0)

@logger
def add_review_polarity(data):
    data.loc[:, 'negative_review_polarity'] = data['negative_review'].apply(get_polarity)
    data.loc[:, 'positive_review_polarity'] = data['positive_review'].apply(get_polarity)

@logger
def parse_tags(data):
    def analize_tags(row):
        tag_list_json_str = row['tags']
        tag_list = json.loads(tag_list_json_str.replace('\'', '"'))
        tags_count = len(tag_list)
        all_tags_joined = ', '.join(tag_list)
        all_tags_words = [w for w in all_tags_joined.split(' ') if w.strip() != '']
        tag_words_count = len(all_tags_words)
        row['tags_count'] = tags_count
        row['tag_words_count'] = tag_words_count
        row['all_tags_joined'] = all_tags_joined
        return row

    data.loc[:, ['tags_count', 'tag_words_count', 'all_tags_joined']] = data.apply(analize_tags, axis=1)

@logger
def recount_review_words(data):
    data.loc[:, 'review_total_negative_word_counts_alt'] = data['negative_review'].apply(count_words)
    data.loc[:, 'review_total_positive_word_counts_alt'] = data['positive_review'].apply(count_words)

@logger
def parse_days_since_review(data):
    data.loc[:, 'days_since_review_int'] = data['days_since_review'].apply(lambda x: int(x.split(' ')[0]))

@logger
def add_time_features(data):
    data['review_date'] = pd.to_datetime(data['review_date'])

    def set_month_year(row):
        review_date = row['review_date']
        day = review_date.day
        month = review_date.month
        year = review_date.year
        row['month'] = str(month)
        row['year'] = str(year)
        row['is_new_year'] = month == 1 and day <= 5
        row['is_xmas'] = month == 12 and day >= 25
        return row

    data.loc[:, ['month', 'year', 'is_new_year', 'is_xmas']] = data.apply(set_month_year, axis=1)

# @logger
# def replace_all_tags_with_tags_polarity(data):
#     def calc_polarity(text):
#         return TextBlob(text).sentiment.polarity

#     data['tags_polarity'] = data['all_tags_joined'].apply(calc_polarity)
#     # data.drop(columns=['all_tags_joined'], inplace=True)
#     pass

