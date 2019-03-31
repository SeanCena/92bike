from points import *
import numpy as np
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.preprocessing import normalize
from clusterPlot import plotCluster

import matplotlib.pyplot as plt


num_clusters = 2000
features = np.array(points)


# def nmap(x, in_min, in_max, out_min, out_max):
  # return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# l1 = [i[0] for i in features]
# l2 = [i[1] for i in features]

# min1 = min(l1)
# max1 = max(l1)
# min2 = min(l2)
# max2 = max(l2)

features = features[~np.all(features == 0, axis=1)]
# features = np.array([[nmap(f[0], min1, max1, 0, 1), nmap(f[1], min2, max2, 0, 1)] for f in features])

kmeans = MiniBatchKMeans(n_clusters=num_clusters, random_state=0).fit(features)

#plotCluster(kmeans, features)
#print(kmeans.labels_[0])

#features = normalize(features, axis=1, norm='l1')
#for f in features:
#  print(f)
#plt.scatter(features[:,1],features[:,0])
#plt.show()

#file = open("getpoints.js", "w")
#file.write("function getPoints() { return [")
for i in range(num_clusters):
    w = kmeans.labels_[i]
    p = kmeans.cluster_centers_[w]
    print("{location: new google.maps.LatLng(" + str(p[0]) + "," + str(p[1]) + "), weight: " + str(w) + "},\n")

print("] }\n")
