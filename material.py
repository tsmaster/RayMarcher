import raymarch
import bdgmath

import sky

class Reflect:
    def __init__(self, color, kR, kD, kA):
        self.baseColor = color
        self.kR = kR
        self.kD = kD
        self.kA = kA

    def evalColor(self, hitPoint, lightList, hitNorm, toViewerVec, scene, recursionDepth):
        nDotV = hitNorm.dot(toViewerVec)
        reflectedVector = hitNorm.mulScalar(2*nDotV).subVec3(toViewerVec)

        reflectedRay = bdgmath.Ray(hitPoint, hitPoint.addVec3(reflectedVector))

        refObj, refPoint, refNorm = raymarch.raymarch(scene, reflectedRay)
        if refObj is None:
            refColor = sky.calcSky(reflectedRay)
        else:
            if ((refObj.material is None) or (recursionDepth == 0)):
                refColor = refObj.evalColorAtPoint(refPoint)
            else:
                refColor = refObj.material.evalColor(refPoint, lightList, refNorm, hitPoint.subVec3(refPoint), scene, recursionDepth - 1)

        cList = [0, 0, 0]

        for component in range(3):
            cList[component] += self.baseColor[component] * self.kA
            cList[component] += refColor[component] * self.kR

        return tuple(cList)
    
