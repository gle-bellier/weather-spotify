import pandas as pd


class Playlist:
    """Spotify Playlist class, aggregating metadata about the playlist's track
    """
    def __init__(self, API, playlist_uri):
        """Creates the Spotify playlist

        Args:
            API (spotipy client): Spotipy client used for accessing the Spotify API
            playlist_uri (str): Spotify uri of the desired playlist 
        """

        self.API = API
        self.playlist_uri = playlist_uri
        self.metadata = None

    def get_playlist_items(self):
        """Accesses the tracks of the playlist

        Returns:
            [dict]: Data about the playlist's tracks
        """
        results = self.API.playlist(self.playlist_uri)
        return results["tracks"]["items"]

    def get_metadata(self):
        """Builds a dataframe with the audio features of the playlist's tracks
        """
        items = self.get_playlist_items()
        uris = [item["track"]["uri"] for item in items]
        features = self.API.audio_features(uris)

        list_data = []

        for idx, item in enumerate(items):
            data = {"name": item["track"]["name"], "uri": item["track"]["uri"]}
            data.update(features[idx])
            list_data.append(data)

        self.metadata = pd.DataFrame(data=list_data,
                                     index=range(len(list_data)))

    def get_means(self):
        """Computes the mean of each audio features in the playlist tracks set

        Returns:
            [pandas.DataFrame]: computed mean for each of the audio features
        """
        if self.metadata is None:
            self.get_metadata()

        # we want only the numerical features
        df = self.metadata.select_dtypes(include=['int64', 'float64'])
        return df.mean()
