from random import randint
s = []
maxc = 0
for i in range(10):
    s.append(randint(0, 5))
sc = s.copy()

for el in s:
    if sc.count(el) > maxc:
        maxc = sc.count(el)
        
print("List:", s)
print("Max count of repeats:", maxc)