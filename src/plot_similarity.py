#from load_songs import *
import sys
import glob
import numpy as np
import matplotlib.cm as cm
import scipy.stats as stats
from scipy.spatial.distance import squareform
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt

import csv

all_features_avg=[]
all_artists=[]
feat_names=[]
features=[]
song_names=[]

line_count=0

with open('new_features.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        if line_count == 0:
            print(row[1] + ', ' + row[4])
            feat_names.append(list(row))
            line_count += 1
        else:
            song_names.append(str(row[1]))
            feat_values=[]
            for i in range(2, 11):
                feat_values.append(row[i])
            line_count += 1
            fv = np.array(feat_values).astype(np.float)
            features.append(fv)
            features_avg=np.mean(features, axis=0)
            all_features_avg.append(features_avg)
    print('Processed {line_count} lines.')
    
#print(feat_names)
#print(feat_values)
print(features)

print(np.shape(all_features_avg))
dist=pdist(all_features_avg)
dist_matrix=squareform(dist)

fig=plt.figure(figsize=(10,10))
ax=fig.add_subplot(111)
x=range(0,len(song_names))
i=ax.imshow(dist_matrix, cmap='nipy_spectral', interpolation='nearest')
plt.xticks(x,song_names,rotation='vertical')
plt.yticks(x,song_names)
plt.tick_params(axis='both', which='major', labelsize=8)
plt.tick_params(axis='both', which='minor', labelsize=8)
fig.colorbar(i, orientation='vertical')
plt.tight_layout()
plt.savefig('Song Similarity Matrix')
plt.show()
