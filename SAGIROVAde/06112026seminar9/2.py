import sys
from math import gcd

sys.setrecursionlimit(200000)


def build(v, tl, tr, arr, tree):
    if tl == tr:
        tree[v] = arr[tl]
    else:
        tm = (tl + tr) // 2
        build(2 * v, tl, tm, arr, tree)
        build(2 * v + 1, tm + 1, tr, arr, tree)
        tree[v] = gcd(tree[2 * v], tree[2 * v + 1])


def query(v, tl, tr, l, r, tree):
    if l > r:
        return 0
    if l == tl and r == tr:
        return tree[v]
    tm = (tl + tr) // 2
    return gcd(query(2 * v, tl, tm, l, min(r, tm), tree),
               query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, tree))

print("Нажмите контрл Д, чтобы увидеть встроенный пример")
data = sys.stdin.read().split()

if data:
    n = int(data[0])
    arr = [int(x) for x in data[1:n + 1]]
    tree = [0] * (4 * n)
    build(1, 0, n - 1, arr, tree)

    k = int(data[n + 1])
    idx = n + 2
    results = []
    for _ in range(k):
        l = int(data[idx]) - 1
        r = int(data[idx + 1]) - 1
        idx += 2
        results.append(str(query(1, 0, n - 1, l, r, tree)))
    print(" ".join(results))
else:
    print("=== Наглядный пример работы ===")
    arr = [12, 18, 24, 30, 42, 56, 72, 90]
    n = len(arr)
    tree = [0] * (4 * n)
    build(1, 0, n - 1, arr, tree)

    print("Исходный массив:", arr)

    queries = [(1, 3), (2, 5), (1, 8), (4, 4)]
    print("\nРезультатЪ:")
    for q in queries:
        ans = query(1, 0, n - 1, q[0] - 1, q[1] - 1, tree)
        print(ans, end=" ")
