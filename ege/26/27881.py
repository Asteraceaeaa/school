"""
    Системный администратор раз в неделю создаёт архив пользовательских файлов. Однако объём диска, куда он помещает архив, может быть меньше, чем суммарный объём архивируемых файлов. Известно, какой объём занимает файл каждого пользователя.

    По заданной информации об объёме файлов пользователей и свободном объёме на архивном диске определите максимальное число пользователей, чьи файлы можно сохранить в архиве, а также максимальный размер имеющегося файла, который может быть сохранён в архиве, при условии, что сохранены файлы максимально возможного числа пользователей.
"""




with open("./27881.txt") as f:
    df = f.read().split()
    d = int(df[0])
    df = [int(x) for x in df[2:]]
    df.sort()
    print(df, d)

sdf = []
for i in df:
    if i not in sdf:
        sdf.append(i)
print(sdf)
c = 0

for i in df:
    if d - i >= 0:
        d -= i
        c += 1
    else:
        j = i
        break
print(f"index of {j} is {sdf.index(j)}")
j = sdf.index(j)

for i in range(1, len(sdf)):
    print(f"{d} - {sdf[j - i]}, {j-i}")
    if d - sdf[j - i] == 0:
        
        maxx = sdf[j - i]
        break

print(c + 1, maxx)