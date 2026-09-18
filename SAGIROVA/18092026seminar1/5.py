"""Task5."""
from numpy import *


n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]


def spyral_matrix_generator(n, m, number, poz_n, poz_m):
    """Generate spyral matrix"""
    matrix[poz_n][poz_m] = number
    number += 1
    if poz_n - 1 != -1 and matrix[poz_n - 1][poz_m] == 0 and (poz_m - 1 == -1 or matrix[poz_n][poz_m - 1] != 0):
        spyral_matrix_generator(n, m, number, poz_n - 1, poz_m)
    elif poz_m + 1 < m and matrix[poz_n][poz_m + 1] == 0:
        spyral_matrix_generator(n, m, number, poz_n, poz_m + 1)
    elif poz_n + 1 < n and matrix[poz_n + 1][poz_m] == 0:
        spyral_matrix_generator(n, m, number, poz_n + 1, poz_m)
    elif poz_m - 1 != -1 and matrix[poz_n][poz_m - 1] == 0:
        spyral_matrix_generator(n, m, number, poz_n, poz_m - 1)
    return 0


spyral_matrix_generator(n, m, 1, 0, 0)
for i in matrix:
    for j in i:
        print(j, end=' ' * (4 - len(str(j))))
    print()
print()

k = 1
for i in matrix:
    i = array(i)
    for j in i * k:
        print(j, end=' ' * (5 - len(str(j))))
    print()
    k += 1
