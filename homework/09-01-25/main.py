bools = [True, False]

for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if not((not x or y) or not(not w or z)):
                    print(*map(int, [z, y, w, x]))
#z y w x
#1 0 0 1
#0 0 0 1
#1 0 1 1