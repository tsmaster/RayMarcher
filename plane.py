import math

class ZPlane:
    def __init__(self, z):
        self.z = z
        self.name = "plane"
        self.color1 = (0, 0.9, 0)
        self.color2 = (0, 0.1, 0)

        self.squareSize = 1
        self.material = None


    def signedDistance(self, point):
        # really, this is a half-space ending at z
        return point.z() - self.z

    def checkerboardColorAtPoint(self, point):
        oddSquareColor = (0.1, 0.1, 0.1)
        evenSquareColor = (0.9, 0.9, 0.9)
        
        x = point.x() % (self.squareSize * 2)
        y = point.y() % (self.squareSize * 2)

        xVal = x > self.squareSize
        yVal = y > self.squareSize

        if xVal == yVal:
            return evenSquareColor
        else:
            return oddSquareColor

    def graphPaperColorAtPoint(self, point):
        lineWidth = self.squareSize / 20

        paperColor = (1, 1, 1)
        lineColor = (.15, .9, .9)

        ss = self.squareSize

        mx = (point.x() + ss * 0.5) % ss - ss * 0.5
        my = (point.y() + ss * 0.5) % ss - ss * 0.5

        ax = abs(mx)
        ay = abs(my)
        if (ax < lineWidth or ay < lineWidth):
            return lineColor
        return paperColor
        
    
    def evalColorAtPoint(self, point):
        return self.checkerboardColorAtPoint(point)
        #return self.graphPaperColorAtPoint(point)
