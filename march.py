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

#cam = camera.YCamera(0, -5, 3)
#cam.setViewDistance(2)
#cam.setViewWidth(2)

cam = camera.FreeCamera(bdgmath.Vector3(10, -8, 6),
                        bdgmath.Vector3(0, 0, 5))

scene = scene.Scene()

scene.addLight(light.DirectionalLight(bdgmath.Vector3(-1, 1, -4), 0.8))
scene.addLight(light.AmbientLight(0.2))

scene.addObject(plane.ZPlane(0))
#scene.addObject(plane.ZPlane(-2))
#scene.addObject(sphere.Sphere(bdgmath.Vector3(-0.1, 0, 2.5), 2.5))

s2 = sphere.Sphere(bdgmath.Vector3(3.5, 2, 2), 2)
s2.color1 = (40, 200, 40)
#s2.color2 = (0, 250, 0)
s2.color2 = (40, 200, 40)
#scene.addObject(s2)

s3 = sphere.Sphere(bdgmath.Vector3(-4, 2, 2), 2)
s3.color1 = (40, 40, 200)
#s3.color2 = (0, 0, 250)
s3.color2 = s3.color1
#scene.addObject(s3)

#cyl = cylinder.ZCylinder(bdgmath.Vector2(1, 4), 1)
#scene.addObject(cyl)

donut = donut.Donut(2.5, 1)
#scene.addObject(donut)

repeat = repeated2d.Repeated2d(9, 9, donut)
#scene.addObject(repeat)

box = box.Box(bdgmath.Vector3(3, 2, 1))
translatedBox = transform.Translate3d(bdgmath.Vector3(0, 5, 1), box)
#scene.addObject(box)
#scene.addObject(translatedBox)

translatedDonut = transform.Translate3d(bdgmath.Vector3(0, 5, 5.5), transform.RotateZ(20, transform.RotateX(80, donut)))
#scene.addObject(translatedDonut)

repeatedBox = repeated2d.Repeated2d(10, 10, transform.Translate3d(bdgmath.Vector3(0, 0, 1), box))
scene.addObject(repeatedBox)
repeatedDonut = repeated2d.Repeated2dBig(10, 10, transform.Translate3d(bdgmath.Vector3(0, 0, 5.5), transform.RotateZ(20, transform.RotateX(80, donut))))
scene.addObject(repeatedDonut)


#cam.renderScene(scene, 80, 45, "raytest.png")
#cam.renderScene(scene, 200, 150, "raytest.png")
#cam.renderScene(scene, 600, 400, "raytest.png")

frame_width = 320
frame_aspect = 2.35
frame_height = int(frame_width / frame_aspect)

anim_duration = 20 # seconds
frames_per_second = 16
num_frames = anim_duration * frames_per_second

start_angle = -45
angle_per_frame = 360 / num_frames

for frame_num in range(num_frames):
    outFilename = "frame_%06d.png" % frame_num
    print (f"frame: {frame_num} / {num_frames}")

    if os.path.exists(outFilename):
        print("exists")
        continue
    
    angle = (start_angle + angle_per_frame * frame_num) % 360
    angleRad = math.radians(angle)
    
    orbitRadius = 12
    camX = orbitRadius * math.cos(angleRad)
    camY = orbitRadius * math.sin(angleRad)
    
    cam.pos = bdgmath.Vector3(camX, camY, 6)
    

    
    cam.renderScene(scene, frame_width, frame_height, outFilename)
