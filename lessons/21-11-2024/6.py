#6.1
"""
    append() - append to end of list
    pop(index) - delete element at index
    remove(el) - delete el from list


"""

l = [1, 2, 3, 4]
print(f"Initial list: {l}")
l.append(1000)
print(f"l.append(1000): {l}")
l.pop(4)
print(f"l.pop(4): {l}")
l.remove(2)
print(f"l.remove(2): {l}")

def maxn(l):
    maxN = 0
    for i in l:
        if maxN < i:
            maxN = i
    return maxN
# print(maxn(l))