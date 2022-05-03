#!/Users/ev/opt/anaconda3/bin/python

import sys

DEBUG = '-d' in sys.argv

EXCLUDE_FROM_TRAINING = [
    'days_since_review_int',
    'lat',
    'lng',
    'city_center_lat',
    'city_center_lng',
    'hotel_address_0',
    'reviewer_nationality_0',
]

INDEX_COLUMN_NAME = None

RANDOM_STATE = 13

SOURCE_DIR = '../data/'
# SOURCE_DIR = '../input/sf-booking/'

TARGET_COLUMN_NAME = 'reviewer_score'

TEST_SIZE = 0.25

FEATURES_TO_NORM = [
    'additional_number_of_scoring',
    'review_total_negative_word_counts',
    'total_number_of_reviews',
    'review_total_positive_word_counts',
    'total_number_of_reviews_reviewer_has_given',
    'distance_to_city_center_km',
    'review_total_negative_word_counts_alt',
    'review_total_positive_word_counts_alt',
    # 'days_since_review_int',
    'tags_count',
    # 'lat',
    # 'lng',
    # 'city_center_lat',
    # 'city_center_lng',
]

FEATURES_TO_STND = [
    'average_score',
    'negative_review_polarity',
    'positive_review_polarity',
    'tag_words_count',
    'tags_polarity',
]

NUM_COLUMNS = [
    'additional_number_of_scoring',
    'average_score',
    'review_total_negative_word_counts',
    'total_number_of_reviews',
    'review_total_positive_word_counts',
    'total_number_of_reviews_reviewer_has_given',
    'distance_to_city_center_km',
    'negative_review_polarity',
    'positive_review_polarity',
    'review_total_negative_word_counts_alt',
    'review_total_positive_word_counts_alt',
    # 'days_since_review_int',
    'tags_count',
    'tag_words_count',
    'tags_polarity',
]

CAT_COLUMNS = [
    # 'lat',
    # 'lng',
    # 'city_center_lat',
    # 'city_center_lng',
    'is_center',
    'is_walking_distance',
    'is_not_far',
    'is_far',
    'is_far_away',
    'is_new_year',
    'is_xmas',
    'hotel_city_1',
    'hotel_city_2',
    'hotel_city_3',
    'hotel_city_4',
    'hotel_city_5',
    'hotel_city_6',
    'month_1',
    'month_2',
    'month_3',
    'month_4',
    'month_5',
    'month_6',
    'month_7',
    'month_8',
    'month_9',
    'month_10',
    'month_11',
    'month_12',
    'year_1',
    'year_2',
    'year_3',
    # 'hotel_address_0',
    'hotel_address_1',
    'hotel_address_2',
    'hotel_address_3',
    'hotel_address_4',
    'hotel_address_5',
    'hotel_address_6',
    'hotel_address_7',
    'hotel_address_8',
    'hotel_address_9',
    'hotel_address_10',
    # 'reviewer_nationality_0',
    'reviewer_nationality_1',
    'reviewer_nationality_2',
    'reviewer_nationality_3',
    'reviewer_nationality_4',
    'reviewer_nationality_5',
    'reviewer_nationality_6',
    'reviewer_nationality_7',
]