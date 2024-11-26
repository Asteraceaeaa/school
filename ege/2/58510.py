"""
    https://inf-ege.sdamgia.ru/problem?id=58510
"""
F1 = lambda w, x, y, z: (w or not y) <= (z == x)
F2 = lambda w, x, y, z: (w or not y) == (z <= x)

f = open("58510.txt", "a")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if F1(w, x, y, z) and not F2(w, x, y, z):
                    f.write(f"{w, x, y, z} \n")
f.close()