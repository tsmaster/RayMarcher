

class RoundEdge:
    def __init__(self, r, obj):
        self.r = r
        self.obj = obj
        self.material = obj.material
        self.color = obj.color

    def signedDistance(self, point):
        return self.obj.signedDistance(point) - self.r

    def evalColorAtPoint(self, point):
        return self.obj.evalColorAtPoint(point)
