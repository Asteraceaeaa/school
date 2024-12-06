"""
    Алгоритм вычисления значения функции F(n), где n  — целое число, задан следующими соотношениями:

    F(n) если n < 15 

    если 

     

    Определите количество значений n, не превышающих 3 ** 40, для которых F(n) = 7560
    """
memo = {}

def F(n):
    if n in memo:
        return memo[n]

    if n < 15:
        res = n
    if n >= 15:
        res = F(n % 15) * F(n // 15)

    memo[n] = res
    return res


target = 7560
limit = 3**40 
res = []


for n in range(1, 3 ** 12):
    if n % 15 != 0:
        c = F(n)
        if c == 7560:
            res.append(n)
print(len(res), res)
 # Ограничение по n

divs = []
for i in res:
    for j in range(1, 1030):
        if i % j == 0:
            print(f"{i} % {j} = 0")
            if j not in divs:
                divs.append(j)
divs.sort()
print(divs, len(divs))


# 3 ** 10 [10, 11, 12, 13, 15, 16, 17, 18, 19]
