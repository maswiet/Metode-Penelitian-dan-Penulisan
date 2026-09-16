"""Pembaca geometri GeoPackage (header GPKG + WKB) tanpa pustaka GIS."""
import struct


def gpkg_geom(blob):
    assert blob[:2] == b"GP", "bukan blob GeoPackage"
    flags = blob[3]
    env = (flags >> 1) & 0x07
    nenv = {0: 0, 1: 4, 2: 6, 3: 6, 4: 8}[env]
    off = 8 + nenv * 8
    return wkb(blob[off:])


def wkb(b):
    pos = 0

    def rd(fmt, n):
        nonlocal pos
        v = struct.unpack_from(fmt, b, pos)
        pos += n
        return v

    def geom():
        nonlocal pos
        bo = b[pos]; pos += 1
        e = "<" if bo == 1 else ">"
        (typ,) = rd(e + "I", 4)
        t = typ % 1000
        if t == 1:      # Point
            return ("Point", list(rd(e + "dd", 16)))
        if t == 2:      # LineString
            (n,) = rd(e + "I", 4)
            pts = rd(e + "%dd" % (2 * n), 16 * n)
            return ("LineString", [(pts[2 * i], pts[2 * i + 1]) for i in range(n)])
        if t == 3:      # Polygon
            (nr,) = rd(e + "I", 4)
            rings = []
            for _ in range(nr):
                (n,) = rd(e + "I", 4)
                pts = rd(e + "%dd" % (2 * n), 16 * n)
                rings.append([(pts[2 * i], pts[2 * i + 1]) for i in range(n)])
            return ("Polygon", rings)
        if t in (4, 5, 6, 7):   # Multi*/Collection
            (ng,) = rd(e + "I", 4)
            return ("Multi", [geom() for _ in range(ng)])
        raise ValueError("tipe geometri %d belum didukung" % t)

    return geom()
