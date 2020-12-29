from PIL import Image

import multiprocessing
import threading
import queue
import time

import bdgmath
import raymarch
import sky

def rayWorker(rayQueue):
    while True:
        rayTask = rayQueue.get()
        px, py, r, scene, img, imgLock, recursionDepth = rayTask

        #if py == 0:
        #    print(f'Working on {px}')
        
        hitObj, hitPoint, norm = raymarch.raymarch(scene, r)

        if hitObj is None:
            color = sky.calcSky(r)
        else:
            if hitObj.material:
                color = hitObj.material.evalColor(
                    hitPoint,
                    scene.lights,
                    norm,
                    r.start.subVec3(hitPoint).makeUnit(),
                    scene,
                    recursionDepth)
            else:
                color = hitObj.evalColorAtPoint(hitPoint)

            accumLight = 0
            for light in scene.lights:
                accumLight += light.evalLight(hitPoint, norm, scene)

            lightFactor = accumLight / scene.lightMax

            cr, cg, cb = color
                    
            color = (cr * lightFactor,
                     cg * lightFactor,
                     cb * lightFactor)

        iColor = tuple([int(c * 255.9) for c in color])

        imgLock.acquire()
        img.putpixel((px, py), iColor)
        if py == 0:
            img.save("working.png")
        imgLock.release()

        #if py == 0:
        #    print(f'Finished {px}')
        rayQueue.task_done()
        

class YCamera:
    def __init__(self, x, y, z):
        self.pos = bdgmath.Vector3(x, y, z)
        self.viewDistance = 1
        self.aspectRatio = 1
        self.viewWidth = 1

    def setViewDistance(self, dist):
        self.viewDistance = dist

    def setViewWidth(self, width):
        """
        this is actually the half width, the X distance from the axis to
        the left or right sides
        """
        self.viewWidth = width

    def renderScene(self, scene, width, height, filename):
        img = Image.new("RGB", (width, height))
        
        leftX = self.pos.x() - self.viewWidth
        rightX = self.pos.x() + self.viewWidth

        self.aspectRatio = width / height

        viewHeight = self.viewWidth / self.aspectRatio
        
        topZ = self.pos.z() + viewHeight
        bottomZ = self.pos.z() - viewHeight

        # xStep goes left to right
        xStep = (rightX - leftX) / (width - 1)

        # zStep goes DOWN
        zStep = (bottomZ - topZ) / (height - 1)

        sy = self.pos.y() + self.viewDistance

        rayQueue = queue.Queue(maxsize = 0)
        imgLock = threading.Lock()
        
        num_threads = multiprocessing.cpu_count()
        print (f"using {num_threads} threads")

        start_time = time.time()
        
        for i in range(num_threads):
            worker = threading.Thread(target = rayWorker, args = (rayQueue,))
            worker.setDaemon(True)
            worker.start()
        
        for px in range(0, width):
            #print ("x: %d(/%d)" % (px, width))
            sx = leftX + xStep * px
            for py in range(0, height):
                sz = topZ + zStep * py

                screenPos = bdgmath.Vector3(sx, sy, sz)
                
                r = bdgmath.Ray(self.pos, screenPos)

                rayQueue.put((px, py, r, scene, img, imgLock))

            #img.save(filename)
        print("all tasks sent")
        rayQueue.join()
        print("all tasks completed")
        img.save(filename)
        print("elapsed time:", time.time() - start_time)




class FreeCamera:
    def __init__(self, pos, target):
        self.pos = pos
        self.target = target
        self.up = bdgmath.Vector3(0, 0, 1)
        self.viewDistance = 1
        self.viewWidth = 1

    def setViewDistance(self, dist):
        self.viewDistance = dist

    def setViewWidth(self, width):
        """
        this is actually the half width, the world X distance from the
        axis to the left or right sides
        """
        self.viewWidth = width

    def renderScene(self, scene, width, height, filename,  recursionDepth):
        img = Image.new("RGB", (width, height))

        aspectRatio = width / height
        
        toTarget = self.target.subVec3(self.pos)
        rightVec = toTarget.cross(self.up).makeUnit().mulScalar(self.viewWidth)
        upVec = rightVec.cross(toTarget).makeUnit().mulScalar(self.viewWidth / aspectRatio)
        stepRight = rightVec.mulScalar(1.0 / (width - 1))
        stepDown = upVec.mulScalar(-1.0 / (height - 1))

        screenCenter = self.pos.addVec3(toTarget.makeUnit().mulScalar(self.viewDistance))
        screenCorner = (screenCenter.
                        subVec3(stepRight.mulScalar((width - 1) / 2)).
                        subVec3(stepDown.mulScalar((height - 1) / 2)))

        rayQueue = queue.Queue(maxsize = 0)
        imgLock = threading.Lock()
        
        num_threads = multiprocessing.cpu_count()
        print (f"using {num_threads} threads")

        start_time = time.time()
        
        for i in range(num_threads):
            worker = threading.Thread(target = rayWorker, args = (rayQueue,))
            worker.setDaemon(True)
            worker.start()
        
        for px in range(0, width):
            right = stepRight.mulScalar(px)
            for py in range(0, height):
                down = stepDown.mulScalar(py)
                screenPos = screenCorner.addVec3(right).addVec3(down)

                r = bdgmath.Ray(self.pos, screenPos)

                rayQueue.put((px, py, r, scene, img, imgLock, recursionDepth))
        print("all tasks sent")
        rayQueue.join()
        print("all tasks completed")
        img.save(filename)
        print("elapsed time:", time.time() - start_time)

