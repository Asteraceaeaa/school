from random import randint
s = []

for i in range(10):
    s.append(randint(0, 100))

for i in range(len(s)):
    s.pop(0)
print(s)
#or s.clear()