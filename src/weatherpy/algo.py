import os
from pprint import pprint
import pandas as pd
import numpy as np
import seaborn as sns

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from weatherpy.infos import SPOTIPY_REDIRECT_URL, SPOTIPY_CLIENT_SECRET, SPOTIPY_CLIENT_ID
from weatherpy.playlist import Playlist
from weatherpy.subset_sum_algo import get_subset_idx

os.environ["SPOTIPY_CLIENT_ID"] = SPOTIPY_CLIENT_ID
os.environ["SPOTIPY_CLIENT_SECRET"] = SPOTIPY_CLIENT_SECRET
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8000"
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

source = Playlist(sp, "63emxHLY69jlsRJ18UXCU8")
playlist = Playlist(sp, "066ZKIpH5hDMmDd5HnyuWr")

# df = source.get_metadata().select_dtypes(include=['int64', 'float64'])
# print(df)
# df = df.apply(lambda x: (x - x.min()) / (x.max() - x.min()), axis=0)
# print(df)
# # we get the mean of the whished features
# m_features = source.get_means()[["valence", "loudness"]]
# print(m_features.to_numpy())

S = np.random.random((20, 10))
T = np.random.random((1, 10))

print("_____________")
print(get_subset_idx(S, T, 3))
