a = int(input())
b = int(input())

def nod(a, b):
    maxnod = 1
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0 and maxnod < i:
            maxnod = i
    return maxnod
print(nod(a, b))