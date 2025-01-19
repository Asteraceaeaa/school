bools = [True, False]

for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if ((not w or x) and ((not y or z) == (not x or y))):
                    print(*map(int, [x, z, y, w]))

#0 1 1 0
#1 1 1 0
#0 1 0 0