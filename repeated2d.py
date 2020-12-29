import bdgmath

# repeat a primitive along xy plane

class Repeated2d:
    def __init__(self, xPeriod, yPeriod, obj):
        self.xPeriod = xPeriod
        self.yPeriod = yPeriod
        self.obj = obj
        self.material = obj.material

    def mutatePoint(self, point):
        px = (point.x() + 0.5 * self.xPeriod) % self.xPeriod - 0.5 * self.xPeriod
        py = (point.y() + 0.5 * self.yPeriod) % self.yPeriod - 0.5 * self.yPeriod
        return bdgmath.Vector3(px, py, point.z())

    def signedDistance(self, point):
        return self.obj.signedDistance(self.mutatePoint(point))

    def evalColorAtPoint(self, point):
        return self.obj.evalColorAtPoint(self.mutatePoint(point))

class Repeated2dBig:
    def __init__(self, xPeriod, yPeriod, obj):
        self.xPeriod = xPeriod
        self.yPeriod = yPeriod
        self.obj = obj

    def mutations(self, point):
        px = (point.x() + 0.5 * self.xPeriod) % self.xPeriod - 0.5 * self.xPeriod
        py = (point.y() + 0.5 * self.yPeriod) % self.yPeriod - 0.5 * self.yPeriod

        if px < 0:
            xOpts = [px, px + self.xPeriod]
        else:
            xOpts = [px - self.xPeriod, px]
        
        if py < 0:
            yOpts = [py, py + self.yPeriod]
        else:
            yOpts = [py - self.yPeriod, py]

        return [bdgmath.Vector3(xOpt, yOpt, point.z())
                for xOpt in xOpts
                for yOpt in yOpts]

    def signedDistance(self, point):
        minVal = None
        for m in self.mutations(point):
            d = self.obj.signedDistance(m)
            if minVal is None or d < minVal:
                minVal = d
        return minVal

    def evalColorAtPoint(self, point):
        minVal = None
        minMut = None
        for m in self.mutations(point):
            d = self.obj.signedDistance(m)
            if minVal is None or d < minVal:
                minVal = d
                minMut = m
        return self.obj.evalColorAtPoint(minMut)
