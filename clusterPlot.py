import matplotlib.pyplot as plt

def plot(pts):
    px = [x for x, y in pts]
    py = [y for x, y in pts]

    fig, ax = plt.subplots()
    ax.scatter(px, py, c='blue')
    ax.autoscale()
    ax.margins(0.1)
    plt.show()


# Test
from random import random
pts = []
for _ in range(10):
    pts.append((random()*5, random()*5))

plot(pts)
