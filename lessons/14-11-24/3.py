alphabet = ['a', 'e', 'i', 'u', 'y', 'o']
stroka = input().lower()

for i in stroka:
    if i in alphabet:
        index = stroka.index(i, 0, len(stroka))
        stroka = stroka[index - 1:index + 1] + stroka[index + 1]
print(stroka)