from sys import *
setrecursionlimit(10 ** 6)

def F(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * F(n - 1)
print(F(2023) / F(2020))