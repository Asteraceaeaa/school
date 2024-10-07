first = [1, 3, 5, 7, 9]
second = [1, 2, 5, 6, 9]
for i in first:
    if i in second:
        second.remove(i)
print(second)