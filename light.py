import math
import bdgmath
import raymarch

class DirectionalLight:
    # e.g. sunlight, with parallel rays

    def __init__(self, lightDirection, lightStrength):
        self.backDir = lightDirection.mulScalar(-1).makeUnit()
        self.lightStrength = lightStrength
        self.castShadows = True

    def evalLight(self, point, normal, scene):
        #print("evaluating light at", point)
        #print("norm:", normal)
        #print("light dir:", self.backDir)
        dot = normal.dot(self.backDir)
        #print("dot:", dot)

        if dot <= 0:
            return 0

        if self.castShadows:
            shadowRay = bdgmath.Ray(point, point.addVec3(self.backDir))
            sObj, sPt, sNorm = raymarch.raymarch(scene, shadowRay)

            if sObj is None:
                # unshadowed
                return dot * self.lightStrength
            else:
                # in shadow
                return 0
        else:
            # no shadows
            return dot * self.lightStrength

        


class AmbientLight:
    def __init__(self, lightStrength):
        self.lightStrength = lightStrength

    def evalLight(self, point, normal, scene):
        return self.lightStrength
