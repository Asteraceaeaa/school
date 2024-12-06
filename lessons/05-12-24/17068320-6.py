from sys import *
setrecursionlimit(100000000)

def F(n):
    if n == 0:
        return 0
    elif n > 0 and n % 3 == 2:
        return F(n - 1) + 1
    elif n > 0 and n % 3 < 2:
        return F((n - n % 3) / 3)
print(F(6))