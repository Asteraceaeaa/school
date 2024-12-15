


def F(x, y, i = 0):
    
    if x == y and i <= 5:
        return 1
    elif i > i or x > y:
        return 0
    else:
        return F(x + 1, y, i + 1) + F(x * 2, y, i + 1)

y = 1

while F(1, y):
    y += 1
print(y)