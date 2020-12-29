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


cam = camera.FreeCamera(bdgmath.Vector3(8, -12, 10),
                        bdgmath.Vector3(-2, 8, 0.75))

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
    w = csg.SmoothDifference(w, c, 0.2)

scene.addObject(w)


cube = box.Box(bdgmath.Vector3(5, 5, 5))
cube.color = (1.0, 0.75, 0.25)

negSphere = sphere.Sphere(bdgmath.Vector3(2.5, -2.5, 2.5), 4.5)

cubeMinusSphere = csg.Difference(cube, negSphere)

torus = donut.Donut(3.5, 1)
torus.color = torus.color1 = torus.color2 = (0, 0.8, 0)

rotTorus = transform.RotateZ(225, transform.RotateX(45, torus))

torusCube = csg.Union(cubeMinusSphere, rotTorus)

posTorusCube = transform.Translate3d(bdgmath.Vector3(-3, 12, 5), torusCube)

scene.addObject(posTorusCube)


cam.renderScene(scene, 640, 320, "raytest.png", 5)
#cam.renderScene(scene, 300, 240, "raytest.png", 5)
#cam.renderScene(scene, 100, 80, "raytest.png", 5)

