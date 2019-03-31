
import numpy as np
from random import random
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
from collections import deque


class Line():
    def __init__(self, p0, p1):
        self.p = np.array(p0)
        self.dirn = np.array(p1) - np.array(p0)
        self.dist = np.linalg.norm(self.dirn)
        self.dirn /= self.dist # normalize

    def path(self, t):
        return self.p + t * self.dirn


def Intersection(line, center, radius):
    a = np.dot(line.dirn, line.dirn)
    b = 2 * np.dot(line.dirn, line.p - center)
    c = np.dot(line.p - center, line.p - center) - radius * radius

    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return False

    t1 = (-b + np.sqrt(discriminant)) / (2 * a);
    t2 = (-b - np.sqrt(discriminant)) / (2 * a);

    if (t1 < 0 and t2 < 0) or (t1 > line.dist and t2 > line.dist):
        return False

    return True


# p0 = (0., 0.)
# p1 = (1., 1.)
# center = (1., 0.)
# radius1 = 1. / np.sqrt(2) + 0.01
# radius2 = 1. / np.sqrt(2) - 0.01
#
# line = Line(p0, p1)
# print(Intersection(line, center, radius1)) # True
# print(Intersection(line, center, radius2)) # False
# print(Intersection(line, (0.5, 0.5), radius1)) # True
# print(Intersection(line, (2., 2.), radius1)) # False
# print(Intersection(line, (-1., -1.), radius1)) # False



def distance(x, y):
    return np.linalg.norm(np.array(x) - np.array(y))


def isInObstacle(vex):
    for obs in obstacles:
        if distance(obs, vex) < radius:
            return True
    return False


def isThruObstacle(line, obstacles):
    for obs in obstacles:
        if Intersection(line, obs, radius):
            return True
    return False


def nearest(G, vex):
    Nvex = None
    Nidx = None
    minDist = float("inf")

    for idx, v in enumerate(G.vertices):
        line = Line(v, vex)
        if isThruObstacle(line, obstacles):
            continue

        dist = distance(v, vex)
        if dist < minDist:
            minDist = dist
            Nidx = idx
            Nvex = v

    return Nvex, Nidx


def newVertex(randvex, nearvex):
    dirn = np.array(randvex) - np.array(nearvex)
    length = np.linalg.norm(dirn)
    dirn = (dirn / length) * min (stepSize, length)

    newvex = (nearvex[0]+dirn[0], nearvex[1]+dirn[1])
    return newvex


class Graph:

    def __init__(self, startpos, endpos):
        self.startpos = startpos
        self.endpos = endpos
        self.vertices = [startpos]
        self.edges = []
        self.neighbors = {}
        self.success = False

        self.sx = endpos[0] - startpos[0]
        self.sy = endpos[1] - startpos[1]

    def randomPosition(self):
        rx = random()
        ry = random()

        posx = self.startpos[0] - (self.sx / 2.) + rx * self.sx * 2
        posy = self.startpos[1] - (self.sy / 2.) + ry * self.sy * 2
        return posx, posy


# startpos = (0., 0.)
# endpos = (3., 2.)
# G = Graph(startpos, endpos)
# G.randomPosition()


def RRT(startpos, endpos):
    G = Graph(startpos, endpos)

    for _ in range(n_iter):
        randvex = G.randomPosition()
        if isInObstacle(randvex):
            continue

        nearvex, nearidx = nearest(G, randvex)
        if nearvex is None:
            continue

        newvex = newVertex(randvex, nearvex)

        G.edges.append((nearidx, len(G.vertices)))
        G.vertices.append(newvex)

        if distance(newvex, G.endpos) < radius:
            G.edges.append((len(G.vertices)-1, len(G.vertices)))
            G.vertices.append(G.endpos)
            G.success = True
            print('success')
            # break
    return G


# startpos = (0., 0.)
# endpos = (5., 5.)
# obstacles = [(1., 1.), (2., 2.)]
# n_iter = 100
# radius = 0.5
#
# G = RRT(startpos, endpos)

def dijkstra(G):
    srcIdx = G.vertices.index(G.startpos)
    dstIdx = G.vertices.index(G.endpos)

    # Preprocess neighbor & distance
    G.neighbors.clear()

    for e1, e2 in G.edges:
        dist = distance(G.vertices[e1], G.vertices[e2])
        v = G.neighbors.get(e1, [])
        v.append((e2, dist))
        G.neighbors[e1] = v

        v = G.neighbors.get(e2, [])
        v.append((e1, dist))
        G.neighbors[e2] = v

    # build dijkstra
    nodes = list(G.neighbors.keys())
    dist = {node: float('inf') for node in nodes}
    prev = {node: None for node in nodes}
    dist[srcIdx] = 0

    while nodes:
        curNode = min(nodes, key=lambda node: dist[node])
        nodes.remove(curNode)
        if dist[curNode] == float('inf'):
            break

        for neighbor, cost in G.neighbors[curNode]:
            newCost = dist[curNode] + cost
            if newCost < dist[neighbor]:
                dist[neighbor] = newCost
                prev[neighbor] = curNode

    # retrieve path
    path = deque()
    curNode = dstIdx
    while prev[curNode] is not None:
        path.appendleft(G.vertices[curNode])
        curNode = prev[curNode]
    path.appendleft(G.vertices[curNode])
    return list(path)

# if G.success:
#     dijkstra(G)

def plot(G, path=None):
    px = [x for x, y in G.vertices]
    py = [y for x, y in G.vertices]
    fig, ax = plt.subplots()

    for obs in obstacles:
        circle = plt.Circle(obs, radius, color='red')
        ax.add_artist(circle)

    ax.scatter(px, py, c='cyan')
    ax.scatter(startpos[0], startpos[1], c='black')
    ax.scatter(endpos[0], endpos[1], c='black')

    lines = [(G.vertices[edge[0]], G.vertices[edge[1]]) for edge in G.edges]
    lc = mc.LineCollection(lines, colors='green', linewidths=2)
    ax.add_collection(lc)

    if path is not None:
        paths = [(path[i], path[i+1]) for i in range(len(path)-1)]
        lc2 = mc.LineCollection(paths, colors='blue', linewidths=3)
        ax.add_collection(lc2)

    ax.autoscale()
    ax.margins(0.1)
    plt.show()



if __name__ == '__main__':
    startpos = (0., 0.)
    endpos = (5., 5.)
    obstacles = [(1., 1.), (2., 2.)]
    n_iter = 200
    radius = 0.5
    stepSize = 0.7

    G = RRT(startpos, endpos)

    if G.success:
        path = dijkstra(G)
        print(path)
        plot(G, path)
    else:
        plot(G)
