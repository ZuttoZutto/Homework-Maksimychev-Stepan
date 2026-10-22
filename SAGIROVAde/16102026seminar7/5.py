"""Task5. Heappsortt"""
def sift_down(a, i, n):
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < n and a[left] > a[largest]:
            largest = left
        if right < n and a[right] > a[largest]:
            largest = right
        if largest == i:
            return
        a[i], a[largest] = a[largest], a[i]
        i = largest


a = [6, 4, 7, 1, 9, -2]
n = len(a)

for i in range(n // 2 - 1, -1, -1):
    sift_down(a, i, n)

for end in range(n - 1, 0, -1):
    a[0], a[end] = a[end], a[0]
    sift_down(a, 0, end)

print(*a)