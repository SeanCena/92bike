from points import *
import numpy as np
from sklearn.cluster import KMeans

num_clusters = 50
features = np.array(points)
kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(features)

#print(kmeans(whitened,book))
print(kmeans.labels_[:num_clusters])

file = open("getpoints.js", "w")
file.write("function getPoints() { return [")
for i in range(num_clusters):
    p = kmeans.cluster_centers_[kmeans.labels_[i]]
    file.write("new google.maps.LatLng(" + str(p[0]) + "," + str(p[1]) + "),\n")

file.write("] }")
