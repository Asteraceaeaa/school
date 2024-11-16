N = int(input("Enter your number => "))

def krat(x):
    if x % 5 == 0 and x % 3 == 0:
        return x

Ns = [krat(i) for i in range(1, N + 1)]
print([x for x in Ns if x is not None])
for i in range(1, N + 1):
    if krat(i):
        print(i)