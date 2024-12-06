

def F(n):
    if n < 3:
        return 1
    elif n > 2:
        return sum([i for i in range(n)])
    
print(F(18))