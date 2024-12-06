


def F(n):
    if n >= 2025:
        return n
    elif n < 2025:
        return n + 3 + F(n + 3)
    
print(F(23)- F(21))