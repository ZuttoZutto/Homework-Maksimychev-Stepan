"""Task3."""
import sys
from math import *


def euclide(a, b):
    """Realise Euclide's theorem"""
    nod = gcd(a, b)
    x = 0
    while True:
        if (nod - a * x) / b % 1 == 0:
            return map(int, [x, (nod - a * x) / b, nod])
        elif (nod + a * x) / b % 1 == 0:
            return map(int, [-1 * x, (nod + a * x) / b, nod])
        x += 1


for string in sys.stdin:
    print(*euclide(*map(int, string.split())))