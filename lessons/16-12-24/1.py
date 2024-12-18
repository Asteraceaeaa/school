from itertools import *

words = ["".join(x) for x in product('abc', repeat=5)]
# print(["".join(x) for x in combinations('aqlghr', 5)])
print(words)
res = []
for w in words:
    if (w[0] == 'a' and not len(w) != 5) and (w[2] == 'b' or not w[4] != 'a') and w.count('c') == 0:
        res.append(w)

print(res)


 