from random import randint
num = randint(1,100000000)
for i in range(1,100000000):
    if i == num:
        print(i)
    else:
        continue