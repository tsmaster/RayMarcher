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



cam = camera.FreeCamera(bdgmath.Vector3(8, -12, 8),
                        bdgmath.Vector3(0, 0, 5))

scene = scene.Scene()

scene.addLight(light.DirectionalLight(bdgmath.Vector3(-1, 0.5, -4), 0.8))
scene.addLight(light.AmbientLight(0.2))

floor = plane.ZPlane(0)
floor.squareSize = 2
scene.addObject(floor)

cube = box.Box(bdgmath.Vector3(5, 5, 5))
cube.color = (1.0, 0.75, 0.25)

negSphere = sphere.Sphere(bdgmath.Vector3(2.5, -2.5, 2.5), 4.5)

cubeMinusSphere = csg.Difference(cube, negSphere)

torus = donut.Donut(3.5, 1)
torus.color = torus.color1 = torus.color2 = (0, 0.8, 0)

rotTorus = transform.RotateZ(225, transform.RotateX(45, torus))

torusCube = csg.Union(cubeMinusSphere, rotTorus)

posTorusCube = transform.Translate3d(bdgmath.Vector3(0, 0, 5), torusCube)

scene.addObject(posTorusCube)


#cam.renderScene(scene, 640, 320, "raytest.png", 5)
cam.renderScene(scene, 100, 80, "raytest.png", 5)

