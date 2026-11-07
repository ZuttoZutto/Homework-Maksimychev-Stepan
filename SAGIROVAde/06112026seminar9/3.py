import sys

sys.setrecursionlimit(200000)


def build(v, tl, tr, arr, tree):
    if tl == tr:
        tree[v] = 1 if arr[tl] == 0 else 0
    else:
        tm = (tl + tr) // 2
        build(2 * v, tl, tm, arr, tree)
        build(2 * v + 1, tm + 1, tr, arr, tree)
        tree[v] = tree[2 * v] + tree[2 * v + 1]


def count_zeros(v, tl, tr, l, r, tree):
    if l > r or r < tl or l > tr:
        return 0
    if l == tl and r == tr:
        return tree[v]
    tm = (tl + tr) // 2
    return count_zeros(2 * v, tl, tm, max(l, tl), min(r, tm), tree) + \
        count_zeros(2 * v + 1, tm + 1, tr, max(l, tm + 1), min(r, tr), tree)


def find_kth_zero(v, tl, tr, l, r, k, tree):
    if tl == tr:
        return tl
    tm = (tl + tr) // 2
    left_zeros = count_zeros(2 * v, tl, tm, l, min(r, tm), tree)
    if k <= left_zeros:
        return find_kth_zero(2 * v, tl, tm, l, min(r, tm), k, tree)
    else:
        return find_kth_zero(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, k - left_zeros, tree)
print("Нажмите контрл Д, чтобы увидеть встроенный пример")

data = sys.stdin.read().split()

if data:
    n = int(data[0])
    arr = [int(x) for x in data[1:n + 1]]
    tree = [0] * (4 * n)
    build(1, 0, n - 1, arr, tree)

    m = int(data[n + 1])
    idx = n + 2
    results = []

    for _ in range(m):
        l = int(data[idx]) - 1
        r = int(data[idx + 1]) - 1
        k = int(data[idx + 2])
        idx += 3
        ans = find_kth_zero(1, 0, n - 1, l, r, k, tree)
        results.append(str(ans + 1))

    print(" ".join(results))
else:
    print("=== Наглядный пример работы ===")
    arr = [1, 0, 2, 0, 3, 0, 4, 0]
    n = len(arr)
    tree = [0] * (4 * n)

    build(1, 0, n - 1, arr, tree)

    print("массив:", arr)

    queries = [(1, 8, 2), (3, 7, 1), (2, 6, 2)]
    print("\nВыполнение запросов:")
    for l, r, k in queries:
        ans = find_kth_zero(1, 0, n - 1, l - 1, r - 1, k, tree)
        print(ans+1, end=" ")