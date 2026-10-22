"""Task1. Minimal heap"""
a = [1, 3, 2, 7, 4, 5]
n = len(a)

ok = True
for i in range(n // 2):
    left = 2 * i + 1
    right = 2 * i + 2
    if a[i] > a[left]:
        ok = False
        break
    if right < n and a[i] > a[right]:
        ok = False
        break

print(1 if ok else 0)