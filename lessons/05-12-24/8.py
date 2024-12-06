memo = {}
from sys import *
setrecursionlimit(10 ** 6)

def F(n):
    if n not in memo:
        if n == 1:
            res = 1
            memo[n] = res
        elif n > 1:
            res = n - 2 + F(n - 1)
            memo[n] = res
    else:
        res = memo[n]
    return res
    

print(F(2023) - F(2021))