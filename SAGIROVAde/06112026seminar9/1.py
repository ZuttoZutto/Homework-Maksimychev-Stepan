
import sys


def build_max_tree(n, arr):
    tree = [0] * (2 * n)
    for i in range(n):
        tree[n + i] = arr[i]
    for i in range(n - 1, 0, -1):
        tree[i] = max(tree[2 * i], tree[2 * i + 1])
    return tree


def get_max(tree, n, left, right):
    l = left - 1 + n
    r = right - 1 + n
    res = 0
    while l <= r:
        if l % 2 == 1:
            if tree[l] > res:
                res = tree[l]
            l += 1
        if r % 2 == 0:
            if tree[r] > res:
                res = tree[r]
            r -= 1
        l //= 2
        r //= 2
    return res


def solve(input_data=None):
    if input_data is None:
        input_data = sys.stdin.read()

    data = input_data.split()
    if not data:
        return False

    n = int(data[0])
    arr = [int(x) for x in data[1:n + 1]]
    tree = build_max_tree(n, arr)

    k = int(data[n + 1])
    idx = n + 2
    results = []

    for _ in range(k):
        l = int(data[idx])
        r = int(data[idx + 1])
        idx += 2
        results.append(str(get_max(tree, n, l, r)))

    print(" ".join(results))
    return True


if __name__ == '__main__':
    print("Нажмите контрл Д, чтобы увидеть встроенный пример")
    if not solve():
        print("=== Наглядный пример работы ===")

        demo_input = """8
1 3 2 7 9 11 4 5
4
1 3
2 5
1 8
4 4"""

        print(demo_input)
        print("\nРезультат")

        solve(demo_input)

        n = 8
        arr = [1, 3, 2, 7, 9, 11, 4, 5]
        tree = build_max_tree(n, arr)

        print("\nвнутреннее дерево отрезков:")
        print(tree)