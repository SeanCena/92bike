
obstacle = []
startpts = (0., 0.)
endpts = (1., 1.)

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



class Graph:

    def __init__(self, startpos, endpos):
        self.startpos = startpos
        self.endpos = endpos
        self.vertices = [startpos]
        self.edges = []

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


def RRT():
    n_iter = 10
    it = 0
    radius = 0.1

    G = Graph()

    for _ in n_iter:
        newvex = G.randomPosition()
        if isInObstacle(newvex):
            continue

        Nvex, Nidx = nearest(G, vex)
        if Nvex is None:
            continue

        G.edges.append((Nidx, len(G.vertices)))
        G.vertices.append(newvex)
