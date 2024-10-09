stroka = list(input())

for i in range(0, stroka.count('e')):
    stroka.remove('e')
for i in range(0, stroka.count('a')):
    stroka.remove('a')
for i in range(0, stroka.count('o')):
    stroka.remove('o')
print(''.join(stroka))