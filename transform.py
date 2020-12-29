import math
import bdgmath

class Translate3d:
    def __init__(self, deltaVec, obj):
        self.deltaVec = deltaVec
        self.obj = obj
        self.color = obj.color
        self.material = None

    def mutatePoint(self, point):
        return point.subVec3(self.deltaVec)

    def signedDistance(self, point):
        return self.obj.signedDistance(self.mutatePoint(point))

    def evalColorAtPoint(self, point):
        return self.obj.evalColorAtPoint(self.mutatePoint(point))
        
class RotateX:
    def __init__(self, rxDeg, obj):
        self.rxRad = math.radians(rxDeg)
        self.obj = obj
        self.material = None
        self.color = obj.color

    def mutatePoint(self, point):
        r = -self.rxRad
        
        nx = point.x()
        ny = point.y() * math.cos(r) - point.z() * math.sin(r)
        nz = point.y() * math.sin(r) + point.z() * math.cos(r)

        return bdgmath.Vector3(nx, ny, nz)

    def signedDistance(self, point):
        return self.obj.signedDistance(self.mutatePoint(point))

    def evalColorAtPoint(self, point):
        return self.obj.evalColorAtPoint(self.mutatePoint(point))
        

class RotateY:
    def __init__(self, ryDeg, obj):
        self.ryRad = math.radians(ryDeg)
        self.obj = obj
        self.material = None
        self.color = obj.color

    def mutatePoint(self, point):
        r = -self.ryRad
        
        ny = point.x()
        nz = point.z() * math.cos(r) - point.x() * math.sin(r)
        nx = point.z() * math.sin(r) + point.x() * math.cos(r)

        return bdgmath.Vector3(nx, ny, nz)

    def signedDistance(self, point):
        return self.obj.signedDistance(self.mutatePoint(point))

    def evalColorAtPoint(self, point):
        return self.obj.evalColorAtPoint(self.mutatePoint(point))
        

class RotateZ:
    def __init__(self, rzDeg, obj):
        self.rzRad = math.radians(rzDeg)
        self.obj = obj
        self.material = None
        self.color = obj.color

    def mutatePoint(self, point):
        r = -self.rzRad
        
        nz = point.z()
        nx = point.x() * math.cos(r) - point.y() * math.sin(r)
        ny = point.x() * math.sin(r) + point.y() * math.cos(r)

        return bdgmath.Vector3(nx, ny, nz)

    def signedDistance(self, point):
        return self.obj.signedDistance(self.mutatePoint(point))

    def evalColorAtPoint(self, point):
        return self.obj.evalColorAtPoint(self.mutatePoint(point))
        

