"""Task4."""

def triangle_generator(size, symb):
    """Generate triangle"""
    massive = [i + 1 for i in range(size)]
    if size % 2 == 0:
        massive = massive + list(reversed(massive))
    else:
        massive = massive + list(reversed(massive))[1:]
    for i in massive:
        print(symb * i)


inp = input()
i, symb = inp.split()
triangle_generator(int(i), symb)