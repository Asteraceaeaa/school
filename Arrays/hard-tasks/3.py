from random import randint
s = []

for i in range(10):
    s.append(randint(0, 100))

sc = s.copy(); sc.sort()
print(f"List: {s}\n2nd maximum is {sc[-2]}")