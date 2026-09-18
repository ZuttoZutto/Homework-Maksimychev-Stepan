"""Task2."""


def spliter(n):
    """Split number into comultypliers."""
    if n == 0:
        return "Don't have"
    elif n == 1:
        return 1
    comultypliers = []
    while n != 1:
        for i in list(range(2, int(n ** 0.5) + 1)) + [n]:
            if n % i == 0:
                n = n / i
                comultypliers.append(int(i))
                break
    return comultypliers


i = int(input())
print(spliter(i))
