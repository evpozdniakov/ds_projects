#!/Users/ev/opt/anaconda3/bin/python

import pandas as pd

# local modules
import constants
from helpers import debug_print
from cleaning import clean_data
from selecting import select_features
from transformation import transform_features
import training

# LOAD DATA
# hotels_test_orig = pd.read_csv(constants.SOURCE_DIR + 'hotels_test.csv.zip', sep=',')
# hotels_train_orig = pd.read_csv(constants.SOURCE_DIR + 'hotels_train.csv.zip', sep=',')
# submission_orig = pd.read_csv(constants.SOURCE_DIR + 'submission.csv.zip', sep=',')

def save_featured_train_set():
    train_data = pd.read_csv(constants.SOURCE_DIR + 'hotels_train.csv.zip', sep=',')
    debug_print(f'shape before: {train_data.shape}')
    training.prepare_data(train_data, is_train_set=True)
    debug_print(f'shape after: {train_data.shape}')
    train_data.to_csv('hotels_train_featured.csv', index=False)
    train_data[0:3000].to_csv('hotels_train_featured_part.csv', index=False)

def save_featured_test_set():
    test_data = pd.read_csv(constants.SOURCE_DIR + 'hotels_test.csv.zip', sep=',')
    print(f'shape before: {test_data.shape}')
    training.prepare_data(test_data, is_train_set=False)
    print(f'shape after: {test_data.shape}')
    test_data.to_csv('hotels_test_featured.csv', index=False)

def prepare(data):
    transform_features(data)
    select_features(data)

def make_submission_out_of_featured_set():
    # LOAD FEATURED TRAIN SET
    X_train = pd.read_csv('hotels_train_featured.csv')

    # PREPARE TRAIN DATA
    prepare(X_train)

    # TRAIN MODEL
    y_train = X_train[constants.TARGET_COLUMN_NAME]
    training.train_model(X_train, y_train)

    # LOAD FEATURED TEST SET
    X_test = pd.read_csv('hotels_test_featured.csv')

    # PREPARE TEST DATA
    prepare(X_test)

    y_pred = training.predict(X_test)
    submission = pd.read_csv(constants.SOURCE_DIR + 'submission.csv.zip', sep=',')
    submission[constants.TARGET_COLUMN_NAME] = y_pred
    submission.to_csv('hotels_prediction.csv', index = False)

def estimate():
    # LOAD FEATURED TRAIN SET
    hotels_featured = pd.read_csv('hotels_train_featured.csv')

    X_train, X_test, y_train, y_test = training.split_to_train_test(hotels_featured)

    # PREPARE TRAIN DATA
    prepare(X_train)

    # TRAIN MODEL
    training.train_model(X_train, y_train)

    # PREPARE TEST DATA
    prepare(X_test)

    # ESTIMATE
    training.estimate_model(X_test, y_test)

# training.prepare_data(X_test)
# training.estimate_model(X_test, y_test)

# make_submission_out_of_featured_set()
# estimate()
print('\nDONE\n')
