

# A capillo usque ad ungues
# Imperare sibI MaxImUm iMperium est
knowns = ["E", "S", "M"]
stroka = "Imperare sibI MaxImUm iMperium est"
indexes = []
unknowns = []
res = [None] * 3
c = 0
print(stroka)
for i in range(len(stroka)):
    ch = stroka[i]
    if ch in knowns and len(indexes) < 2:
        indexes.append(i)
    elif ch not in knowns and ch not in unknowns:
        unknowns.append(ch)

if len(indexes) < 1:
    res[0] = 0; res[1] = len(stroka)
elif len(indexes) == 1:
    res[0] = indexes[0] + 1; res[1]  =  len(stroka) - indexes[0] - 1
else:
    res[0] = indexes[0] + 1; res[1] = indexes[1] - indexes[0] - 1
    

res[2] = [ch for ch in unknowns if ch != " "]
print(res[0], res[1], len(res[2]))  