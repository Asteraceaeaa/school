
memo = {}
def F(n):
    if n not in memo:

        if n < 10:
            res = n
            
        elif n >= 10:
            res = F(n % 10) + F(n // 10)
        memo[n] = res
        return memo[n]
    
    return memo[n]
d = True
memos = {}

for n in range(11 ** 13 + 9, 11 ** 13 + 10680009, 10):
    f = F(n)

    memos[n] = f
with open("output.txt", "w") as ff:
    for i in memos:
        
            ff.write(f"{i}, {memos[i]}\n")

