
def F(n):
    if n == 0:
        return 0
    elif n > 0 and n % 3 == 2:
        return F(n - 1) + 1
    elif n > 0 and n % 3 < 2:
        return F((n - n % 3) / 3)
minn = 100000
m = 10000
while m != 0:
    if minn > F(m) and F(m) == 5:
        minn = m
    m -= 1
print(minn)

