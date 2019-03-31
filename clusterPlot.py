import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from random import random
import numpy as np

def plot(pts):
    px = [x for x, y in pts]
    py = [y for x, y in pts]

    fig, ax = plt.subplots()
    ax.scatter(px, py, c='blue')
    ax.autoscale()
    ax.margins(0.1)
    plt.show()


def plotCluster(kmeans, points):
    x = points[:,0]
    y = points[:,1]
    ctrx = kmeans.cluster_centers_[:, 0]
    ctry = kmeans.cluster_centers_[:, 1]
    label = kmeans.labels_

    colors = []
    for _ in range(kmeans.n_clusters):
        colors.append((random(), random(), random()))

    fig = plt.figure(figsize=(12,12))
    
    plt.scatter(ctrx, ctry, c='black', marker='x', s=30)
    plt.scatter(x, y, c=label, cmap=matplotlib.colors.ListedColormap(colors),s=5)

    cb = plt.colorbar()
    loc = np.arange(0,max(label),max(label)/float(len(colors)))
    cb.set_ticks(loc)
    cb.set_ticklabels(list(range(kmeans.n_clusters)))
    plt.show()



# Test
# pts = []
# for _ in range(10):
#     pts.append((random()*5, random()*5))
#
# plot(pts)
