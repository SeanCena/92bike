
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
    minDist = float("inf")

    for v in G.vertices:
        line = Line(v, vex)
        if isThruObstacle(line, obstacles):
            continue

        dist = distance(v, vex)
        if dist < minDist:
            minDist = dist
            Nvex = v

    return Nvex, minDist



class Graph:

    def __init__(self):
        vertices = []
        edges = []

    def randomPosition(self):
        pass


def RRT():
    pass
