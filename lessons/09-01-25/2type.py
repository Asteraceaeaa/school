bools = [True, False]

print("x y z w")
usl = lambda x, y, z, w: (x == (w or y)) or ((not w or z) and (not y or w)) 
#Импликация <= || not x or y

for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if usl(x, y, z, w) is False:
                    res = [int(i) for i in [y, x, z, w]]
                    print(f"{res} == {usl(x, y, z, w)}")