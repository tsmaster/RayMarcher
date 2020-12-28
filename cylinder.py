# an infinite cylinder

import math
import bdgmath

class ZCylinder:
    def __init__(self, basePoint2d, radius):
        self.base = basePoint2d
        self.radius = radius
        self.color = (200, 200, 0)

    def signedDistance(self, point):
        vecToAxis2d = bdgmath.Vector2(point.x() - self.base.x(),
                                      point.y() - self.base.y())
        distToAxis = vecToAxis2d.mag()
        return distToAxis - self.radius

    def evalColorAtPoint(self, point):
        return self.color

