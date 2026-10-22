"""Task4. Potugno"""
import sys

data = """4
3 6 8 10 15
1 5 12
4 8 15 16
2 6
""".splitlines()

n = int(data[0].strip())

values = []
for idx in range(n):
    for token in data[idx + 1].split():
        values.append((int(token), idx))

values.sort()

count = [0] * n
have = 0
left = 0
best_len = None
best_l = best_r = None

for right, (value, idx) in enumerate(values):
    if count[idx] == 0:
        have += 1
    count[idx] += 1

    while have == n:
        left_value = values[left][0]
        length = value - left_value

        if best_len is None or length < best_len:
            best_len = length
            best_l, best_r = left_value, value

        left_idx = values[left][1]
        count[left_idx] -= 1
        if count[left_idx] == 0:
            have -= 1
        left += 1

print(f"{best_l}–{best_r}")