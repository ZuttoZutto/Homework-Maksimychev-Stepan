"""Task1."""


def fibonacci(n):
    """Calculate fibonacci number."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


i = int(input())
print(fibonacci(i))
