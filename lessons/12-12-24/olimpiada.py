
with open("russian_names_dataset.txt") as f:
    data = [el.split(' ') for el in f.read().split("\n")]
    # print(data)

def to_dict(key, data):
    slovar = maxes = {}

    for i in data:
        if i[key] not in slovar.keys():
            slovar[i[key]] = i
        else:
            slovar[i[key]] += i
    # print(slovar['10'])
    # print(slovar)
    for i in '9', '10', '11':

        # print(slovar[i])
        # name_of_max = ''
        maxx = 0
        # print(type(slovar[i][-1]))
        # print(slovar[i])
        
        if type(slovar[i][-1]) == list:
            
            for j in slovar[i]:
                # print(j, i)

                if maxx < int(j[-1]):
                    maxx = int(j[-1])
        else:
            
            maxx = int(slovar[i][-1])
        maxes[i] = maxx
        maxx = 0 
    return maxes

print(to_dict(2, data))

# to_classes = [[], [], []]
# maxes = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# for i in data:
#     match i[2]:
#         case "9":
#             to_classes[0].append(i)
#         case "10":
#             to_classes[1].append(i)
#         case "11":
#             to_classes[2].append(i)

# print(to_classes)
# for i in range(len(to_classes)):
#     for j in range(len(to_classes[i])):
#         x, y = to_classes[i][j], maxes[i]  
#         print(x, y)
#         xx, yy = int(x[-1]), int(y[-1])
#         if xx > yy:
#             maxes.remove(y)
#             maxes.append(x)


# print(maxes)
# classes = [9, 10, 11]
# maxes =    [0, 0, 0]
# names =   ['', '', '']

