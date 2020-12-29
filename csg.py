# supports CSG operations
import bdgmath

class Difference:
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2
        self.material = obj1.material
        self.color = obj1.color

    def signedDistance(self, point):
        d1 = self.obj1.signedDistance(point)
        d2 = self.obj2.signedDistance(point)
        return max(d1, -d2)

    def evalColorAtPoint(self, point):
        return self.obj1.evalColorAtPoint(point)


class Intersection:
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2
        self.material = obj1.material
        self.color = obj1.color

    def signedDistance(self, point):
        d1 = self.obj1.signedDistance(point)
        d2 = self.obj2.signedDistance(point)
        return max(d1, d2)

    def evalColorAtPoint(self, point):
        return self.obj1.evalColorAtPoint(point)


class Union:
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2
        self.material = obj1.material
        self.color = obj1.color

    def signedDistance(self, point):
        d1 = self.obj1.signedDistance(point)
        d2 = self.obj2.signedDistance(point)
        return min(d1, d2)

    def evalColorAtPoint(self, point):
        d1 = self.obj1.signedDistance(point)
        d2 = self.obj2.signedDistance(point)
        if d1 < d2:
            return self.obj1.color
        return self.obj2.color


    
    
# supports smooth CSG operations


class SmoothDifference:
    def __init__(self, obj1, obj2, k):
        self.obj1 = obj1
        self.obj2 = obj2
        self.k = k
        self.material = obj1.material
        self.color = obj1.color

    def signedDistance(self, point):
        d1 = self.obj1.signedDistance(point)
        d2 = self.obj2.signedDistance(point)

        h = bdgmath.clamp(0.5 - 0.5 * (d1 + d2) / self.k, 0, 1)

        return bdgmath.mapVal(h, 0, 1, d1, -d2) + self.k * h * (1.0 - h)

    def evalColorAtPoint(self, point):
        return self.obj1.evalColorAtPoint(point)


class SmoothIntersection:
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2
        self.material = obj1.material
        self.color = obj1.color

    def signedDistance(self, point):
        d1 = self.obj1.signedDistance(point)
        d2 = self.obj2.signedDistance(point)

        h = bdgmath.clamp(0.5 - 0.5 * (d2 - d1) / self.k, 0, 1)

        return bdgmath.mapVal(h, 0, 1, d2, d1) + self.k * h * (1.0 - h)

    def evalColorAtPoint(self, point):
        return self.obj1.evalColorAtPoint(point)


class SmoothUnion:
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2
        self.material = obj1.material
        self.color = obj1.color

    def signedDistance(self, point):
        d1 = self.obj1.signedDistance(point)
        d2 = self.obj2.signedDistance(point)

        h = bdgmath.clamp(0.5 - 0.5 * (d2 - d1) / self.k, 0, 1)

        return bdgmath.mapVal(h, 0, 1, d2, d1) - self.k * h * (1.0 - h)

    def evalColorAtPoint(self, point):
        return self.obj1.evalColorAtPoint(point)



    
    
