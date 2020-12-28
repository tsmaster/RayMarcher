import math

class ZPlane:
    def __init__(self, z):
        self.z = z
        self.name = "plane"
        self.color1 = (0, 200, 0)
        self.color2 = (0, 20, 0)

        self.squareSize = 1


    def signedDistance(self, point):
        # really, this is a half-space ending at z
        return point.z() - self.z

    def checkerboardColorAtPoint(self, point):
        x = point.x() % (self.squareSize * 2)
        y = point.y() % (self.squareSize * 2)

        xVal = x > self.squareSize
        yVal = y > self.squareSize

        if xVal == yVal:
            return self.color1
        else:
            return self.color2

    def graphPaperColorAtPoint(self, point):
        lineWidth = self.squareSize / 20

        paperColor = (255, 255, 255)
        lineColor = (40, 225, 225)

        ss = self.squareSize

        mx = (point.x() + ss * 0.5) % ss - ss * 0.5
        my = (point.y() + ss * 0.5) % ss - ss * 0.5

        ax = abs(mx)
        ay = abs(my)
        if (ax < lineWidth or ay < lineWidth):
            return lineColor
        return paperColor
        
    
    def evalColorAtPoint(self, point):
        return self.graphPaperColorAtPoint(point)
