N  = int(input())
summ = 1 + (1 + N / 10)

for i in range(1, N):
    summ += 1 + i / 10
print(summ)