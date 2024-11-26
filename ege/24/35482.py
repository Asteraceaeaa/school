"""

    Текстовый файл содержит строки различной длины.
    Общий объём файла не превышает 1 Мбайт. 
    Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
    Необходимо найти строку, содержащую наименьшее количество букв G (если таких строк несколько, надо взять ту, которая находится в файле раньше), и определить, какая буква встречается в этой строке чаще всего.
    Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.

"""

with open("35482.txt") as f:
    data = [s.strip() for s in f.readlines()]
    # print(data)
maxx = 1019
min_index = 0
for i in range(len(data)):
    c = 0
    for l in data[i]:
        if l == "G":
            c += 1
    if maxx > c:
        maxx = c
        min_index = i

uniques = []
uniq_indexes = []

for i in data[min_index]:
    if i not in uniques:
        uniques.append(i)
uniques.sort(reverse=True)
for i in range(len(uniques)):
    c = data[min_index].count(uniques[i])
    uniq_indexes.append(c)

maxc = 0
letter = 0
for i in range(len(uniq_indexes)):
    if maxc < uniq_indexes[i]:
        maxc, letter = uniq_indexes[i], uniques[i]

print(letter)