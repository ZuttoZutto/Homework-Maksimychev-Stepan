"""Task1. Vectoris"""
import math


class Vector:
    def __init__(self, x, y=None, z=None):
        if isinstance(x, str):
            x, y, z = [float(t) for t in x.strip("{} ").split(",")]
        assert isinstance(x, (int, float))
        assert isinstance(y, (int, float))
        assert isinstance(z, (int, float))
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, o):
        return Vector(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o):
        return Vector(self.x - o.x, self.y - o.y, self.z - o.z)

    def __mul__(self, o):
        if isinstance(o, Vector):
            return self.x*o.x + self.y*o.y + self.z*o.z
        return Vector(self.x*o, self.y*o, self.z*o)

    def __rmul__(self, o):
        return self * o

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"


def center_of_mass(pts):
    s = Vector(0, 0, 0)
    for p in pts:
        s = s + p
    return s * (1 / len(pts))


def area(a, b, c):
    u = b - a
    v = c - a
    cx = u.y*v.z - u.z*v.y
    cy = u.z*v.x - u.x*v.z
    cz = u.x*v.y - u.y*v.x
    return abs(Vector(cx, cy, cz)) / 2


def max_triangle(pts):
    n = len(pts)
    best = 0
    best_pts = None
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                s = area(pts[i], pts[j], pts[k])
                if s > best:
                    best = s
                    best_pts = (pts[i], pts[j], pts[k])
    return best, best_pts


points = [
    Vector("{0, 0, 0}"),
    Vector("{1, 0, 0}"),
    Vector("{0, 1, 0}"),
    Vector("{0, 0, 1}"),
]
print("центр масс:", center_of_mass(points))
s, tri = max_triangle(points)
print("макс площадь:", s)
print("точки:", tri)