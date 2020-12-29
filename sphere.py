import math
import bdgmath

class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.name = "sphere"
        self.color1 = (200, 60, 30)
        self.color2 = (250, 30, 0)
        self.material = None

    def signedDistance(self, point):
        vecToCenter = point.subVec3(self.center)
        distToCenter = vecToCenter.mag()
        return distToCenter - self.radius

    def evalColorAtPoint(self, point):
        if self.material:
            lights = []
            norm = bdgmath.Vector3(0, 0, 1)
            toViewer = bdgmath.Vector3(1, -1, 1)
            return self.material.evalColor(point, lights, norm, toViewer)
        else:
            if point.z() < self.center.z():
                return self.color2
            return self.color1
