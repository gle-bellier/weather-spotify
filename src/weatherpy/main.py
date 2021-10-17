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
from weatherpy.algo import get_weather_playlist

os.environ["SPOTIPY_CLIENT_ID"] = SPOTIPY_CLIENT_ID
os.environ["SPOTIPY_CLIENT_SECRET"] = SPOTIPY_CLIENT_SECRET
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8000"
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

source_uri = "63emxHLY69jlsRJ18UXCU8"
destination_uri = "066ZKIpH5hDMmDd5HnyuWr"

# defining the features we want to take into account
features = ["tempo", "acousticness", "liveness"]
target = np.random.random((1, len(features)))

weather_pl = get_weather_playlist(sp, source_uri, destination_uri, target,
                                  features)
print(weather_pl["uri"])
print(weather_pl.columns.values)