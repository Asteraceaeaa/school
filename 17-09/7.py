n = 4
x = 2
S = 0

for i in range(0, n + 1, 2):
    S += x ** (-i)
    print(x ** -i)
print(S)
