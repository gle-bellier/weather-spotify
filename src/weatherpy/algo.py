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
destination = Playlist(sp, "066ZKIpH5hDMmDd5HnyuWr")

# collect tracks audio features (numerical ones)
s_data = source.get_metadata()
d_data = destination.get_metadata()

s = s_data.select_dtypes(include=['int64', 'float64'])
d = d_data.select_dtypes(include=['int64', 'float64'])

# we normalize the source and the destination playlist audio features
norm = lambda x: (x - x.min()) / (x.max() - x.min())
s = s.apply(norm, axis=0)
d = d.apply(norm, axis=0)

print(s)
# defining the features we want to take into account
features = ["tempo", "acousticness", "liveness"]

S = s[features]
target = np.random.random((1, len(features)))

print("_____________")
print(target)
indexes = get_subset_idx(S, target, 3).squeeze()
print(s_data.iloc[list(indexes)])