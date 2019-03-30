
obstacle = []
startpts = (0., 0.)
endpts = (1., 1.)

class Line():
    def __init__(self, p0, p1):
        self.p = np.array(p0)
        self.dirn = np.array(p1) - np.array(p0)
        self.dirn /= np.linalg.norm(self.dirn)

    def path(self, t):
        return self.p + t * self.dirn


def Intersection(line, center, radius):
    a = np.dot(line.dirn, line.dirn)
    b = 2 * np.dot(line.dirn, line.p - center)
    c = np.dot(line.p - center, line.p - center) - radius * radius

    discriminant = b * b - 4 * a * c
    if discriminant >= 0:
        return True
    else:
        return False


# p0 = (0., 0.)
# p1 = (1., 1.)
# center = (1., 0.)
# radius1 = 1. / np.sqrt(2) + 0.01
# radius2 = 1. / np.sqrt(2) - 0.01
#
# line = Line(p0, p1)
# print(Intersection(line, center, radius1)) # True
# print(Intersection(line, center, radius2)) # False


class Graph:

    def __init__(self):
        vertices = []
        edges = []

    def randomPosition(self):
        pass


def RRT():
    pass
