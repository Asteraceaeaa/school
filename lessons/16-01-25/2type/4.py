bools = [True, False]

for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if (((x and y) or (y and z)) == ((not x or w) and (not w or z))):
                    print(*map(int, [x, z, w, y]))