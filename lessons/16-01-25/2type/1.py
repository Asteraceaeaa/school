bools = [True, False]

for x in bools:
    for y in bools:
        for z in bools:
                if (not(x or y) or(y == z)) is False:
                    print(*map(int, [z, x, y]))

#1 1 0
#0 0 1
#0 1 1