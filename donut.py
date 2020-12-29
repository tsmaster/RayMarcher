import math
import bdgmath

import colorsys


# a torus/donut
#   -     -
#  ( )   ( ) 
#   -     -  rb
#      |ra|
#
# ra is the distance from the middle of the hole to a point centered
# inside the bready bit.
# rb is the radius of the bready extrusion

class Donut:
    def __init__(self, ra, rb):
        self.ra = ra
        self.rb = rb
        #self.color1 = (200, 150, 50)
        #self.color2 = (72, 49, 12) #"0x48310c"
        self.color1 = (180, 140, 20) # cake
        self.color2 = (200, 100, 100) # icing
        self.color = self.color1

    def signedDistance(self, point):
        # distance from the z = 0 projection to the center
        planeDist = bdgmath.Vector2(point.x(), point.y()).mag()

        x = planeDist - self.ra
        # this point is in an xy plane cutting through the bread,
        # centered in the center of the bread.
        xzPoint = bdgmath.Vector2(x, point.z())
        return xzPoint.mag() - self.rb

    def evalColorAtPoint(self, point):
        if point.z() > 0:
            theta = math.atan2(point.y(), point.x())
            thetaNorm = theta / (2 * math.pi)
            if thetaNorm < 0:
                thetaNorm += 1
            if thetaNorm > 1:
                thetaNorm -= 1
            rgbNorm = colorsys.hsv_to_rgb(thetaNorm, 0.6, 0.8)
            rN, gN, bN = rgbNorm
            return (int(rN * 255),
                    int(gN * 255),
                    int(bN * 255))
            #return self.color2
        return self.color1



        
