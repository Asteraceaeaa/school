"""
    https://inf-ege.sdamgia.ru/problem?id=14688

"""
print("x y z")

# table = [
#     [1, 0, 0],
#     [1, 0, 1],

# ]   
# tablee = [
#     ["x","y","z"],


# ]
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not((x or y) <= (z == x)):
                print(x, y, z)
#                 tablee.append([x, y, z])
# print(tablee)
