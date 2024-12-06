memo = {}
def F(n):
    if n not in memo:
        if n > 2024:
            res = n
        elif n <= 2024:
            res = n * F(n + 1)
    else:
        res = memo[n]
    return res

print(F(2022) / F(2024))