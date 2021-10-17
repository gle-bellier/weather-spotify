import os
from pprint import pprint
import pandas as pd
import numpy as np
import seaborn as sns

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from weatherpy.infos import SPOTIPY_REDIRECT_URL, SPOTIPY_CLIENT_SECRET, SPOTIPY_CLIENT_ID, WEATHER_API_KEY

from weatherpy.weather import Weather

from weatherpy.playlist import Playlist
from weatherpy.subset_sum_algo import get_subset_idx
from weatherpy.algo import get_weather_playlist

os.environ["SPOTIPY_CLIENT_ID"] = SPOTIPY_CLIENT_ID
os.environ["SPOTIPY_CLIENT_SECRET"] = SPOTIPY_CLIENT_SECRET
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8000"
scope = "user-library-read playlist-modify-public"

w = Weather(WEATHER_API_KEY)
weather = w.get_weather("Paris")
weather_features = list(weather.values())

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

source_uri = "63emxHLY69jlsRJ18UXCU8"
destination_uri = "066ZKIpH5hDMmDd5HnyuWr"

print("Target : ", weather_features)
# defining the features we want to take into account
features = ["tempo", "acousticness", "liveness", "energy"]
target = np.random.random((1, len(features)))

# TODO : make sure the playlist length is > given length(min)
weather_pl = get_weather_playlist(sp,
                                  source_uri,
                                  destination_uri,
                                  target,
                                  features,
                                  nb_tracks=10)

# we need to extract the tracks ids

# TODO : normalize audio features in the playlist
print(weather_pl[features])
track_ids = [elt.split(":")[-1] for elt in list(weather_pl["uri"])]

results = sp.playlist_replace_items(destination_uri, track_ids)
pprint(results)
