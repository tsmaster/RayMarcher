import math
import bdgmath

class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.name = "sphere"
        self.color1 = (200, 60, 30)
        self.color2 = (250, 30, 0)

    def signedDistance(self, point):
        vecToCenter = point.subVec3(self.center)
        distToCenter = vecToCenter.mag()
        return distToCenter - self.radius

    def evalColorAtPoint(self, point):
        if point.z() < self.center.z():
            return self.color2
        return self.color1
