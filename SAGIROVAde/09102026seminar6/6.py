def process_string(s):
    n = len(s)
    if n <= 2:
        return ord(s[0])
    elif n < 10:
        mid = n // 2 if n % 2 == 1 else n // 2 - 1
        return ord(s[0]) + ord(s[mid]) + ord(s[-1])
    else:
        return ord(s[-1])

print(process_string(input().strip()))