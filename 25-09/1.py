n = 20000

#Выясняет длину числа
d = 3
def length(n):
    prev = 0
    for i in range(2, 1000):
        this = n % 10 ** (i + 1)
        if prev == this:
            length = i 
            break
        else:
            prev = this
    return length



for i in range(1000, n + 1):
    l = length()
    if n > 3:
        if (i % 10 == i // 1000 and n % 100 // 10 == n % 1000 // 100):
            print(i)
    else:
        if i % 10 == i // 100:
            print(i)








"""(i % 10 == i // 100) or """
