
#1
bools = [True, False]

usl = lambda x, y, z, w: (not w or x) and ((not y or z) == (not x or y))

for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if usl(x, y, z, w):
                    res = [int(i) for i in [x, z, y, w]]
                    if 0 in res:
                        print(res)


#2
bools = [True, False]

usl = lambda x, y, z, w: ((not x or y) or (y == w)) and ((x or z) == w)

for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if usl(x, y, z, w):
                    res = [int(i) for i in [z, y, x, w]]
                    
                    print(res)

#3
bools = [True, False]

usl = lambda x, y, z, w: ((not x or y) == (not z or w)) or (x and w)
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if usl(x, y, z, w) is False:
                    res = [int(i) for i in [z, y, x, w]]
                    
                    print(res)



#4
bools = [True, False]

usl = lambda x, y, z, w: (x or y) and not(y == z) and not w
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if usl(x, y, z, w) is True:
                    res = [int(i) for i in [x, z, y, w]]
                    
                    print(res)


#5
bools = [True, False]

usl = lambda x, y, z, w: (x and not y) or (y == z) or not w
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if usl(x, y, z, w) is False:
                    res = [int(i) for i in [w, z, y, x]]
                    
                    print(res)

#6
bools = [True, False]

usl = lambda x, y, z, w: (not x or y) or not(not w or z)
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if usl(x, y, z, w) is False:
                    res = [int(i) for i in [z, y, w, x]]
                    
                    print(res)

#7
bools = [True, False]

usl = lambda x, y, z, w: not((x and not y) == (z or not w)) or (x and z)
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if usl(x, y, z, w) is False:
                    res = [int(i) for i in [y, z, w, x]]
                    
                    print(*res)

#8
bools = [True, False]

usl = lambda x, y, z, w: ((not w or not x) == (not z or y)) and (y or w)
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                # if usl(x, y, z, w):
                    res = [int(i) for i in [x, w, y, z]]
                    
                    print(res, usl(x, y, z, w))

#9
bools = [True, False]

usl = lambda x, y, z, w: (x or y) and not (y == z) and not w
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if usl(x, y, z, w) is True:
                    res = [int(i) for i in [z, y, x, w]]
                    
                    print(res)

#10
bools = [True, False]

usl = lambda x, y, z, w: (not(x == y) or (not z or w)) == (not((not w or x) or (not y or z)))
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if usl(x, y, z, w) is True:
                    res = [int(i) for i in [w, z, y, x]]
                    
                    print(res)