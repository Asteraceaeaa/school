K = int(input())
N = int(input())
summ = 0

for i in range(K, N + 1):
    if i % 2 == 0:
        summ += i
print(summ)