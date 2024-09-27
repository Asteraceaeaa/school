n = 10000
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

for i in range(100, n + 1):
    for j in range(2, length(i) + 1):
        print(j)
