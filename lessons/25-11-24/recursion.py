"""import sys
sys.setrecursionlimit(10 ** 6)
sys.set_int_max_str_digits(10 ** 6)

def F(n):
    if n == 1:
        return 3
    return F(n - 1) * (n - 1)

print(F(2026) - F(2024))"""

a, b = 20, 36

def F(n):
    if n == 0:
        return 0
    return F(n-1) + n

c = 0

for i in range(a, b + 1):
    if F(i) % 3 == 0:
        c += 1
print(c)
print(len(range(a // 3 * 3, b + 1, 3)))