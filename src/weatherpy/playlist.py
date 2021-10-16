import os
from pprint import pprint
import pandas as pd

import spotipy
from spotipy.oauth2 import SpotifyOAuth
    from weatherpy.infos import SPOTIPY_REDIRECT_URL, SPOTIPY_CLIENT_SECRET, SPOTIPY_CLIENT_ID

os.environ["SPOTIPY_CLIENT_ID"] = SPOTIPY_CLIENT_ID
os.environ["SPOTIPY_CLIENT_SECRET"] = SPOTIPY_CLIENT_SECRET
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8000"
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


class Playlist:
    def __init__(self, playlist_uri):
        self.playlist_uri = playlist_uri
        self.metadata = None

    def get_playlist_items(self):
        results = sp.playlist(self.playlist_uri)
        return results["tracks"]["items"]

    def get_metadata(self):
        items = self.get_playlist_items()
        uris = [item["track"]["uri"] for item in items]
        names = [item["track"]["name"] for item in items]
        features = sp.audio_features(uris)

        list_data = []

        for idx, item in enumerate(items):
            data = {"name": item["track"]["name"], "uri": item["track"]["uri"]}
            data.update(features[idx])
            list_data.append(data)

        self.metadata = pd.DataFrame(data=list_data,
                                     index=range(len(list_data)))


pl = Playlist("066ZKIpH5hDMmDd5HnyuWr")
pl.get_metadata()
pprint(pl.metadata[["name", "valence"]])
