import os
from pprint import pprint
import pandas as pd
import numpy as np
from weatherpy.playlist import Playlist
from weatherpy.subset_sum_algo import get_subset_idx


def get_weather_playlist(API, source_uri, destination_uri, target, features):

    source = Playlist(API, source_uri)
    destination = Playlist(API, destination_uri)

    # collect tracks audio features (numerical ones)
    s_data = source.get_metadata()
    d_data = destination.get_metadata()

    # check if all features in the playlist audio features
    assert all([feature in s_data.columns.values for feature in features
                ]), "Features not all in Playlist audio features"

    s = s_data.select_dtypes(include=['int64', 'float64'])
    d = d_data.select_dtypes(include=['int64', 'float64'])

    # we normalize the source and the destination playlist audio features
    norm = lambda x: (x - x.min()) / (x.max() - x.min())
    s = s.apply(norm, axis=0)
    d = d.apply(norm, axis=0)

    # we only take into account the given features
    s = s[features]
    indexes = get_subset_idx(s, target, 3).squeeze()
    return s_data.iloc[list(indexes)]