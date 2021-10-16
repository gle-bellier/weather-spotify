import os
from pprint import pprint
import pandas as pd
import seaborn as sns

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from weatherpy.infos import SPOTIPY_REDIRECT_URL, SPOTIPY_CLIENT_SECRET, SPOTIPY_CLIENT_ID
from weatherpy.playlist import Playlist

os.environ["SPOTIPY_CLIENT_ID"] = SPOTIPY_CLIENT_ID
os.environ["SPOTIPY_CLIENT_SECRET"] = SPOTIPY_CLIENT_SECRET
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8000"
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

source = Playlist(sp, "63emxHLY69jlsRJ18UXCU8")
playlist = Playlist(sp, "066ZKIpH5hDMmDd5HnyuWr")

source.get_metadata()
pprint(source.metadata[["name", "valence", "loudness"]])
pprint(source.get_means())

playlist.get_metadata()
pprint(playlist.metadata[["name", "valence", "loudness"]])
pprint(playlist.get_means())
