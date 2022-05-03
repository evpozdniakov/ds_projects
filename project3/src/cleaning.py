import numpy as np
import pandas as pd

# local modules
from helpers import debug_print
from helpers import logger
import constants

@logger
def clean_data(data, is_train_set=False):
    if is_train_set:
        remove_duplicates(data)

    add_missing_coords(data)

    if data.isna().sum().sum() > 0:
        raise ValueError('Data set still has nan after cleaning.')

@logger
def add_missing_coords(data):
    if 'lat' not in data.columns:
        return

    m = data['lat'].isna()

    if m.sum() == 0:
        return

    # Lets try to populate missing lat/lng
    # we have stored some of them in addr_lat_lng.csv
    addr_lat_lng_df = pd.read_csv('address_lat_lng.csv', sep=',')

    def get_lat_lng_by_addr(addr):
        m = addr_lat_lng_df['hotel_address'] == addr
        if m.sum() == 1:
            return addr_lat_lng_df[m][['lat', 'lng']].values[0]
        return [np.nan, np.nan]

    debug_print('Entries with missing lat/lng before:' + str(data['lat'].isna().sum()))

    # TODO use merge
    # loop over hotels without coords
    for index in data[m].index:
        addr = data.loc[index]['hotel_address']
        data.loc[index, ['lat', 'lng']] = get_lat_lng_by_addr(addr)

    debug_print('Entries with missing lat/lng after:' + str(data['lat'].isna().sum()))

@logger
def remove_duplicates(data):
    if constants.INDEX_COLUMN_NAME is not None:
        data.drop(columns=[constants.INDEX_COLUMN_NAME], inplace=True)

    m = data.duplicated()
    
    if m.sum() == 0:
        debug_print('No duplicates found')
        return

    data.drop_duplicates(inplace=True)
    debug_print(f'Removed {m.sum()} duplicated rows')
