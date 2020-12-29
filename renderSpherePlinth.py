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

cam = camera.FreeCamera(bdgmath.Vector3(3, -7, 10),
                        bdgmath.Vector3(0, 0, 4))

scene = scene.Scene()

scene.addLight(light.DirectionalLight(bdgmath.Vector3(-1, 0.5, -4), 0.8))
scene.addLight(light.AmbientLight(0.2))

floor = plane.ZPlane(0)
floor.squareSize = 2
scene.addObject(floor)

s = sphere.Sphere(bdgmath.Vector3(0, 0, 4), 2)
s.material = material.Reflect(
    (0.4, 0.4, 0.4), # base color
    0.5, # kR the amount of reflected light to use
    0.3, # kD the amount of diffuse light to use
    0.2, # kA the amount of ambient light to use
    )
scene.addObject(s)
#repeatedSphere = repeated2d.Repeated2d(10, 10, s)
#scene.addObject(repeatedSphere)

plinth = box.Box(bdgmath.Vector3(1.5, 1.5, 1))
translatedPlinth = transform.Translate3d(bdgmath.Vector3(0, 0, 1), plinth)
scene.addObject(translatedPlinth)

#repeatedPlinth = repeated2d.Repeated2d(10, 10, translatedPlinth)
#scene.addObject(repeatedPlinth)

cam.renderScene(scene, 400, 300, "raytest.png", 5)

