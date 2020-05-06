# shows acoustic features for tracks for the given artist

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False

if len(sys.argv) > 1:
    artist_name = ' '.join(sys.argv[1:])
else:
    artist_name = 'weezer'
    


results = sp.search(q=artist_name, limit=50)
tnames = []
tids = []
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])
    tnames.append(t['name'])
    tids.append(t['uri'])

start = time.time()
features = sp.audio_features(tids)
delta = time.time() - start

id = 1  # Song ID
feature_set = pd.DataFrame()


songname_vector = pd.Series()
energy = pd.Series()
liveness = pd.Series()
tempo = pd.Series()
speechiness = pd.Series()
acousticness = pd.Series()
instrumentalness = pd.Series()
danceability = pd.Series()
loudness = pd.Series()
valence = pd.Series()

for feature in features:
    #print(json.dumps(feature, indent=4))
    print(feature)
    songname_vector.set_value(id, tnames[id-1])
    energy.set_value(id, feature['energy'])
    liveness.set_value(id, feature['liveness'])
    tempo.set_value(id, feature['tempo'])
    speechiness.set_value(id, feature['speechiness'])
    acousticness.set_value(id, feature['acousticness'])
    instrumentalness.set_value(id, feature['instrumentalness'])
    danceability.set_value(id, feature['danceability'])
    loudness.set_value(id, feature['loudness'])
    valence.set_value(id, feature['valence'])
    #print("------------------------------------------------------")
    analysis = sp._get(feature['analysis_url'])
    #print(json.dumps(analysis, indent=4))
    print("######################################################")
    id = id+1
    
feature_set['name'] = songname_vector
feature_set['energy'] = energy
feature_set['liveness'] = liveness
feature_set['tempo'] = tempo
feature_set['speechiness'] = speechiness
feature_set['acousticness'] = acousticness
feature_set['instrumentalness'] = instrumentalness
feature_set['danceability'] = danceability
feature_set['loudness'] = loudness
feature_set['valence'] = valence

feature_set.to_csv('new_features.csv')

print("features retrieved in %.2f seconds" % (delta,))
