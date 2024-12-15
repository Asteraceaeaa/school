

def listSum(seq):
    if not seq:
        return 0
    return seq[0] + listSum(seq[1:])

print(listSum([1, 1, 2, 3, 5, 8, 12]))