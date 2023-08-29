import pandas as pd
import numpy as np
import json
import re

def unravel_lists(
    series_list=[],
    throwaway=[], # contains throwaway series and list items
    reappropriate=False,
    one_hot_columns=[]):

    # if reappropriating list items, one_hot_columns must not be empty
    if reappropriate and not one_hot_columns:
        print("Please provide one_hot_columns in order to fill new dataframe")
        return
    elif reappropriate:
        unraveled_df = pd.DataFrame(np.zeros((len(series_list), len(one_hot_columns))), columns=one_hot_columns)
    elif not series_list:
        print("Please provide list_series in order to return unraveled columns for future dataframe")
    else:
        unraveled_list = []

    # cycle through series of lists and pull out individual items
    for i, row in enumerate(series_list):
        if row not in throwaway:
            contents = row[1:-1] #assuming the list items are given as a list of strings
            items = [item for item in contents.split(', ')]
            for item in items:
                item = item[1:-1]
                if item not in throwaway:
                    if not reappropriate:
                        unraveled_list.append(item)
                    else:
                        unraveled_df.at[i, item] = 1

    if not reappropriate:
        return list(set(unraveled_list))
    else:
        return unraveled_df.to_numpy()
