



def F(n):
    if n ==  1 or n == 2:
        return 3
    elif n > 2:
        return 5 * F(n - 1) - 4 * F(n - 2)
    

print(F(15))