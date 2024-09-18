N  = int(input())
summ = 0

for i in range(1, N + 1):
    summ += i ** (-1)
print(round(summ, 3))