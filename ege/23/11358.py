from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

def f(start, end):
    
    if start > end:
        return 0
    elif start == end:
        return 1
    else:
        return f(start + 1, end) + f(start + 2, end) + f(start * 2, end)

print(f(3, 10) * f(10, 12))