


def calcSky(r):
    hr, hg, hb = (0.4, 0.4, 0.8)
    zr, zg, zb = (0, 0, 0.8)

    rV = r.end.subVec3(r.start).makeUnit()
    rz = rV.z()

    if rz < 0:
        return (hr, hg, hb)

    return ((zr - hr) * rz + hr,
            (zg - hg) * rz + hg,
            (zb - hb) * rz + hb)

