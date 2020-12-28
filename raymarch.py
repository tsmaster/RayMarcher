import bdgmath

EPSILON = 1e-6
TOO_BIG = 1e5


def distToScene(scene, p):
    minDist = None
    closestObj = None
    
    for obj in scene.objects:
        d = obj.signedDistance(p)
        if ((minDist is None) or
            (d < minDist)):
            minDist = d
            closestObj = obj
    return minDist, closestObj

def calcNormal(scene, probePoint):
    step = 0.0001
    
    x, y, z = probePoint.components
    xp = bdgmath.Vector3(x + step, y, z)
    xm = bdgmath.Vector3(x - step, y, z)
    yp = bdgmath.Vector3(x, y + step, z)
    ym = bdgmath.Vector3(x, y - step, z)
    zp = bdgmath.Vector3(x, y, z + step)
    zm = bdgmath.Vector3(x, y, z - step)

    dxp = distToScene(scene, xp)
    dxm = distToScene(scene, xm)
    dyp = distToScene(scene, yp)
    dym = distToScene(scene, ym)
    dzp = distToScene(scene, zp)
    dzm = distToScene(scene, zm)
    
    if dxp[0] and dxm[0]:
        xg = dxp[0] - dxm[0]
    else:
        xg = 0
    if dyp[0] and dym[0]:
        yg = dyp[0] - dym[0]
    else:
        yg = 0
    if dzp[0] and dzm[0]:
        zg = dzp[0] - dzm[0]
    else:
        zg = 0

    n = bdgmath.Vector3(xg, yg, zg)
    return n.makeUnit()

def raymarch(scene, ray):
    maxSteps = 1000
    stepCount = 0
    
    while True:
        if stepCount > maxSteps:
            return None, None, None
        stepCount += 1
        
        probePoint = ray.end

        dist, obj = distToScene(scene, probePoint)
        if dist < EPSILON:
            normal = calcNormal(scene, probePoint)
            return obj, probePoint, normal
        if dist > TOO_BIG:
            return None, None, None
        ray = ray.extend(dist)
        
        
    return None
        

                
