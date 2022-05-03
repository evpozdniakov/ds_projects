import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

# local modules
import constants
from cleaning import clean_data
from creating import create_features
from helpers import logger
from selecting import select_features
from transformation import transform_features

@logger
def split_to_train_test(data):
    X = data.select_dtypes(include=[np.number])
    X.drop(columns=[constants.TARGET_COLUMN_NAME], inplace=True)
    y = data[constants.TARGET_COLUMN_NAME]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=constants.TEST_SIZE, random_state=constants.RANDOM_STATE)

    return X_train, X_test, y_train, y_test

regr_model = None

@logger
def train_model(X_train, y_train):
    if constants.TARGET_COLUMN_NAME in list(X_train.columns):
        X_train = X_train.drop(columns=[constants.TARGET_COLUMN_NAME])

    global regr_model

    regr_model = RandomForestRegressor(n_estimators=50, random_state=constants.RANDOM_STATE)
    regr_model.fit(X_train, y_train)

MAPE = None

@logger
def estimate_model(X_test, y_test):
    global regr_model

    y_pred = predict(X_test)

    global MAPE

    MAPE = metrics.mean_absolute_percentage_error(y_test, y_pred)
    print('MAPE:', MAPE)

@logger
def train_and_estimate(data):
    X_train, X_test, y_train, y_test = split_to_train_test(data)

    train_model(X_train, y_train)

    estimate_model(X_test, y_test)

@logger
def predict(X_test):
    y_pred = regr_model.predict(X_test.select_dtypes(include=[np.number]))

    return y_pred

@logger
def prepare_data(data, is_train_set):
    clean_data(data, is_train_set)
    create_features(data)
    transform_features(data)
    select_features(data)
