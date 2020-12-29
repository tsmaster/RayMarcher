import os
import math
import bdgmath

import camera
import scene

import plane
import sphere
import cylinder
import donut
import box
import repeated2d
import transform
import light
import material
import csg
import roundedge


cam = camera.FreeCamera(bdgmath.Vector3(5, -8, 6),
                        bdgmath.Vector3(0, 0, 0.75))

scene = scene.Scene()

scene.addLight(light.DirectionalLight(bdgmath.Vector3(-1, 0.5, -4), 0.8))
scene.addLight(light.AmbientLight(0.2))

floor = plane.ZPlane(0)
floor.squareSize = 2
scene.addObject(floor)

disk = roundedge.RoundEdge(0.1, cylinder.CappedCylinder(0.8, 3.8))

translatedDisk = transform.Translate3d(bdgmath.Vector3(0, 0, 1.5), disk)
#scene.addObject(translatedDisk)

negCyl1 = cylinder.ZCylinder(bdgmath.Vector2(1.5, 1.5), 1.1)
negCyl2 = cylinder.ZCylinder(bdgmath.Vector2(1.5, -1.5), 1.1)
negCyl3 = cylinder.ZCylinder(bdgmath.Vector2(-1.5, -1.5), 1.1)
negCyl4 = cylinder.ZCylinder(bdgmath.Vector2(-1.5, 1.5), 1.1)

w = translatedDisk
for c in [negCyl1, negCyl2, negCyl3, negCyl4]:
    w = csg.Difference(w, c)

scene.addObject(w)

#cam.renderScene(scene, 640, 320, "raytest.png", 5)
#cam.renderScene(scene, 300, 240, "raytest.png", 5)
cam.renderScene(scene, 100, 80, "raytest.png", 5)

