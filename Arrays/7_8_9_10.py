from random import randint
s = []; maxx = 0

for i in range(10):
    s.append(randint(0, 100))

#7
print(s)
for i in s:
    if maxx < i:
        maxx = i
print("max", maxx) #or max(s)

#8
minn = maxx
for i in s:
    if minn > i:
        minn = i

print("min", minn) #or min(s)

#9 sum
summ = 0
for i in s:
    summ += i
print("sum", summ) #or sum(s)

#10 avg
print("avg", summ / len(s)) 
