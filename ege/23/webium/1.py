
#recursion
def f(start, end, c = 0):
    if start > end:
        return 0
    elif start == end and c == 7:
        return 1
    elif start == end:
        return 0
    return f(start + 1, end, c + 1) + f(start + 4, end, c + 1) + f(start * 2, end, c + 1)
print(f(3,27))