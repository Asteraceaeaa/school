

def F(n):
    if n <= 2:
        return 2
    elif n > 2: 
        return F(n - 2) * (n + 1)
    
print(F(8))