#!/Users/ev/opt/anaconda3/bin/python

# import numpy as np
import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.feature_selection import chi2
# from sklearn.feature_selection import f_classif
# from sklearn import metrics
# import seaborn as sns
# import matplotlib.pyplot as plt
# import category_encoders as ce
# import json
# from textblob import TextBlob
# from scipy import stats
# from sklearn import preprocessing
# from geopy import distance
# import time
# import googlemaps

# local modules
import clean
import features

DEBUG = True
EXCLUDE_FROM_TRAINING = [
    # 'additional_number_of_scoring',
    # 'average_score',
    # 'city_center_lat',
    # 'city_center_lng',
    # 'days_since_review',
    # 'distance_to_city_center_km',
    # 'hotel_address',
    # 'hotel_city',
    # 'hotel_city_1',
    # 'hotel_city_2',
    # 'hotel_city_3',
    # 'hotel_city_4',
    # 'hotel_city_5',
    # 'hotel_city_6',
    # 'hotel_name',
    # 'is_center',
    # 'is_far',
    # 'is_far_away',
    # 'is_not_far',
    # 'is_walking_distance',
    # 'lat',
    # 'lng',
    # 'negative_review',
    # 'positive_review',
    # 'review_date',
    # 'review_total_negative_word_counts',
    # 'review_total_positive_word_counts',
    # 'reviewer_nationality',
    # 'reviewer_score',
    # 'tags',
    # 'total_number_of_reviews',
    # 'total_number_of_reviews_reviewer_has_given',
]
INDEX_COLUMN_NAME = None
RANDOM_STATE = 13
SOURCE_DIR = '../data/'
# SOURCE_DIR = '../input/sf-booking/'
TARGET_COLUMN_NAME = 'reviewer_score'
TEST_SIZE = 0.25

# LOAD DATA
# =========

# hotels_test_orig = pd.read_csv(SOURCE_DIR + 'hotels_test.csv.zip', sep=',')
hotels_train_orig = pd.read_csv(SOURCE_DIR + 'hotels_train.csv.zip', sep=',')
# submission_orig = pd.read_csv(SOURCE_DIR + 'submission.csv.zip', sep=',')
hotels_train = hotels_train_orig.copy()

# hotels_train_orig_part = pd.read_csv('hotels_train_part.csv')
# print('hotels_train_orig_part.shape')
# print(hotels_train_orig_part.shape)
# hotels_train = hotels_train_orig_part[0:1000].copy()
# hotels_train = hotels_train_orig_part.copy()


# GOAL: add all the features and save the result

# CLEAN DATA
clean.add_missing_coords(hotels_train)

# ADD FEATURES
# ============
features.add_all(hotels_train)

hotels_train.to_csv('hotels_train_featured.csv', index=False)

print('\nDONE\n')
