import numpy as np
from pprint import pprint


def get_subset_idx(S, T, n_tracks):
    """Compute the indexes of the n_tracks closets points of S
    to the target T

    Args:
        S (float array): Set of track metadata
        T (float array): Target metadata array
        n_tracks (int): Number of tracks in the output subset

    Returns:
        int array: the n_tracks indexes of the tracks to include in the tracks subset
    """
    # compute the distance of each point to the target
    dist = np.linalg.norm(S - T, axis=1, keepdims=True)
    return dist.argsort(axis=0)


S = np.random.random(size=(10, 3))
T = np.random.random(size=(1, 3))

print(get_subset_idx(S, T, 3))
