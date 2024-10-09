from random import randint
s = []
sc = []

for i in range(10):
    s.append(randint(0, 25))

for el in s:
    if el not in sc:
        sc.append(el)

print("List:", s)
print("Unique elements:", len(sc))
