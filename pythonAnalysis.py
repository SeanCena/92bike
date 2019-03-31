import matplotlib.pyplot as plt
import numpy as np
from points import data
from math import floor
import pdb

step = 0.01 #box size for grid is 0.0001 deg lat/long
minlat = 180
maxlat = -180
minlong = 90
maxlong = -90
maxcrime = 0
pass1 = []
mapweights = []
for i in data:
    if round(i[0], 2) < minlat:
        minlat = round(i[0], 2)
    if round(i[1], 2) < minlong:
        minlong = round(i[1], 2)
    pass1.append([round(i[0], 2), round(i[1], 2)])
for i in pass1:
    i[0] -= minlat
    i[1] -= minlong
    i[0] *= 100
    i[1] *= 100
    if i[0] > maxlat:
        maxlat = i[0]
    if i[1] > maxlong:
        maxlong = i[1]

mapweights = [[0.0 for i in range(int(maxlong)+1)] for j in range(int(maxlat)+1)]
for i in pass1:
    mapweights[int(i[0])][int(i[1])] += 1.0
    #print(mapweights[int(i[0])][int(i[1])])

def scale(X, x_min, x_max):
    nom = (X-X.min(axis=0))*(x_max-x_min)
    denom = X.max(axis=0) - X.min(axis=0)
    denom[denom==0] = 1
    return x_min + nom/denom

temp = np.array(mapweights)
heatmap = scale(temp, 0, 1)

#plt.imshow(heatmap, cmap="hot", interpolation = "nearest")
#plt.show()