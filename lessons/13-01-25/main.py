#1
bools = [True, False]

for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if ((not x or y) and (not y or w) or (z == (x or y))) is False:
                    print(*map(int, [y, w, z, x]))

#0 0 0 1
#1 0 0 1
#1 0 0 0
#0 1 0 1

#2
bools = [True, False]
print("#2")
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if ((x and not y) or (x == z) or not w) is False:
                    print(*map(int, [w, z, y ,x]))

#3
bools = [True, False]
print("#3")
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if (not(not x or w) or (y == z) or y) is False:
                    print(*map(int, [z, x, w ,y]))
#4
bools = [True, False]
print("#4")
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if ((x and not y) or (y == z) or w) is False:
                    print(*map(int, [y, x, w ,z]))
#0 0 0 1
#1 0 0 0
#1 1 0 0

#5
bools = [True, False]
print("#5")
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if (((not w or x) or (not y or z)) and (not(x == y) or (w == z))) is False:
                    print(*map(int, [x, z, w, y]))
#0 0 1 0
#0 0 1 1
#1 0 1 1

#6
bools = [True, False]
print("#6")
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if ((x and not y) or (y == z) or not w) is False:
                    print(*map(int, [w, z, y, x]))
#1 0 1 1
#1 0 1 0
#1 1 0 0