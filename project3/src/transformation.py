import pandas as pd
from sklearn import preprocessing

# local modules
import constants
from helpers import logger

stnd_scaler = None
@logger
def standardize_features(data, features):
    global stnd_scaler

    if stnd_scaler is None:
        stnd_scaler = preprocessing.StandardScaler().fit(data[features])

    ndarr = stnd_scaler.transform(data[features])
    stnd_df = pd.DataFrame(ndarr, columns=[features]).set_index(data.index)
    data.loc[:, features] = stnd_df[features]

norm_scaler = None
@logger
def normalize_features(data, features):
    global norm_scaler

    if norm_scaler is None:
        norm_scaler = preprocessing.MinMaxScaler().fit(data[features])

    ndarr = norm_scaler.transform(data[features])
    norm_df = pd.DataFrame(ndarr, columns=[features]).set_index(data.index)
    data.loc[:, features] = norm_df[features]

@logger
def transform_features(data):
    standardize_features(data, constants.FEATURES_TO_STND)
    normalize_features(data, constants.FEATURES_TO_NORM)
