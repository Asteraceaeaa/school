

def F(n):
    if n < 3:
        return n
    elif n > 2 and n % 2 == 0:
        return int((4 * n - F(n - 3)) / 8)
    elif n > 2 and n % 2 != 0:
        return int((4 * n - F(n-1) + F(n - 2)) / 8)
print(F(52) - F(38))


