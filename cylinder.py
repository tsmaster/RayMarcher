# an infinite cylinder

import math
import bdgmath

class ZCylinder:
    def __init__(self, basePoint2d, radius):
        self.base = basePoint2d
        self.radius = radius
        self.color = (.8, .8, 0)
        self.material = None

    def signedDistance(self, point):
        vecToAxis2d = bdgmath.Vector2(point.x() - self.base.x(),
                                      point.y() - self.base.y())
        distToAxis = vecToAxis2d.mag()
        return distToAxis - self.radius

    def evalColorAtPoint(self, point):
        return self.color

class CappedCylinder:
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
        self.color = (1, 0.5, 0)
        self.material = None
        self.hrVec = bdgmath.Vector2(self.radius, self.height)

    def signedDistance(self, point):
        xyVec = bdgmath.Vector2(point.x(), point.y())
        left = bdgmath.Vector2(xyVec.mag(), abs(point.z()))
        d = left.subVec2(self.hrVec)

        inDist = min(max(d.x(), d.y()), 0.0)
        
        outVec = bdgmath.Vector2(max(d.x(), 0.0), max(d.y(), 0.0))
        return outVec.mag() + inDist

    def evalColorAtPoint(self, point):
        return self.color
