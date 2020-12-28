import math

class Scene:
    def __init__(self):
        self.objects = []
        self.lights = []
        self.lightMax = 1.0

    def addObject(self, obj):
        self.objects.append(obj)

    def addLight(self, light):
        self.lights.append(light)
