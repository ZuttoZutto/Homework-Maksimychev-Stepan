def transform(s):
    if len(s) < 4:
        if all(ch.isupper() for ch in s):
            return s.upper()
        return s
    else:
        count = sum(1 for ch in s[:4] if ch.isupper())
        if count >= 3:
            return s.upper()
        return s

print(transform(input()))