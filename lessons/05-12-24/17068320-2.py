memo = {}
def F(n):
    if n not in memo:
        if n == 0:
            res = 0
        elif n % 2 == 0:
            res = F(n / 2)
        elif n % 2 != 0:
            res = 1 + F(n - 1)
    else:
        res = memo[n]
    return res
c = 0

for n in range(1, 901):
    if F(n) == 9:
        c += 1
print(c)