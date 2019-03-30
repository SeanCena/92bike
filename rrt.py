
obstacle = []
startpts = (0., 0.)
endpts = (1., 1.)

class Intersection:

    def __init__(self, p0, p1):
        self.p = np.array(p0)
        self.dirn = np.array(p1) - np.array(p0)
        self.dirn /= np.linalg.norm(self.dirn)

    def path(self, t):
        return self.p + t * self.dirn


class SphereIntersection(Intersection):

    def __init__(self, p0, p1, center, radius):
        super().__init__(p0, p1)
        self.center = center
        self.radius = radius

    def isInRange(self):
        a = np.dot(self.dirn, self.dirn)
        b = 2 * np.dot(self.dirn, self.p - self.center)
        c = np.dot(self.p - self.center, self.p - self.center) - (self.radius)**2

        discriminant = b * b - 4 * a * c
        if discriminant >= 0:
            return True
        else:
            return False


class Graph:

    def __init__(self):
        vertices = []
        edges = []

    def randomPosition(self):
        pass

    

# p0 = (0., 0.)
# p1 = (1., 1.)
# center = (1., 0.)
# radius = 1. / np.sqrt(2) + 0.01 # True
# radius = 1. / np.sqrt(2) + 0.01 # False
#
# sint = SphereIntersection(p0, p1, center, radius)
# sint.isInRange()

def RRT():
    pass
