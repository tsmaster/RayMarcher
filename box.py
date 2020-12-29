import math
import bdgmath


class Box:
    def __init__(self, corner):
        cx, cy, cz = corner.components
        self.cx = cx
        self.cy = cy
        self.cz = cz
        self.color = (.5, .3, .3)
        self.material = None

    def signedDistance(self, point):
        px, py, pz = point.components

        px = abs(px)
        py = abs(py)
        pz = abs(pz)

        qx = px - self.cx
        qy = py - self.cy
        qz = pz - self.cz
        
        dx = max(0, qx)
        dy = max(0, qy)
        dz = max(0, qz)

        dVec = bdgmath.Vector3(dx, dy, dz)
        outsideDist = dVec.mag()

        insideDist = min(max(qx, qy, qz), 0)
        return outsideDist + insideDist

    def evalColorAtPoint(self, point):
        return self.color
