

def F(n):
    if n < 3:
        return n
    elif n > 2:
        return 3 * F(n - 1) - 2 * F(n - 2)
print(F(7))