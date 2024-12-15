

def F(start, end):
    if start == end:
        return 1
    elif start > end:
        return 0
    else:
        return F(start + 1, end) + F(start + 2, end) + F(start + 3, end)



print(F(1, 8) * F(8, 15))



