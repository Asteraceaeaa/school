l = input().split(' ')
l = [int(x) for x in l]
uq = []
uqc = []




for i in l:
   if i not in uq:
      uq.append(i)
for i in uq:
   uqc.append(l.count(i))

print(uqc)
print(uq)