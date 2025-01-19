bools = [True, False]

for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if (not((not y or x) and (z or w)) or ((x and not w) or (y == z))) is False:
                    print(*map(int, [z, y, x, w]))
#1 
#
#