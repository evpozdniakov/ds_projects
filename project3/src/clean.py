#!/Users/ev/opt/anaconda3/bin/python

import numpy as np
import pandas as pd

# local modules
from helpers import debug_print
from helpers import logger

@logger
def add_missing_coords(data):
    # Lets try to populate missing lat/lng
    # we have stored some of them in addr_lat_lng.csv
    addr_lat_lng_df = pd.read_csv('address_lat_lng.csv', sep=',')

    def get_lat_lng_by_addr(addr):
        m = addr_lat_lng_df['hotel_address'] == addr
        if m.sum() == 1:
            return addr_lat_lng_df[m][['lat', 'lng']].values[0]
        return [np.nan, np.nan]

    debug_print('Entries with missing lat/lng before:' + str(data['lat'].isna().sum()))

    # TODO: use merge
    # loop over hotels without coords
    m = data['lat'].isna()
    for index in data[m].index:
        addr = data.loc[index]['hotel_address']
        data.loc[index, ['lat', 'lng']] = get_lat_lng_by_addr(addr)

    debug_print('Entries with missing lat/lng after:' + str(data['lat'].isna().sum()))
