"""
    Определите количество троек элементов в которых два числа трёхзначные, и сумма элементов тройки меньше максимального элемента последовательности оканчивающегося на 13.
    В ответе запишите два числа: сначала количество найденных троек, а затем минимальную из сумм таких троек. 
    В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
"""

with open("59785.txt") as f:
    data = [int(x) for x in f]
    maxel = max([abs(i) for i in data if i % 100 == 13])
    minel = min(i for i in data if i % 100 == 13)
print(maxel, len(data))
print(data)

def check(ns):
    c = 0
    for i in ns:
        if len(str(abs(i))) == 3:
            c += 1
    return c


count = 0
m = 1000000
for i in range(len(data) - 2):
    a, b, c = data[i], data[i + 1], data[i + 2]
    ns = [a, b, c]

    if sum(ns) < maxel and check(ns) == 2:
        count += 1
        # print(check(ns), ns)
        m = min(m, sum(ns))

print(count, m)



