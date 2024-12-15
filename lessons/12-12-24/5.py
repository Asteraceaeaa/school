# N = 10
# with open("data.txt", "w") as f:
#     ns = [x for x in range(100)]
#     for i in ns:
#         f.write(str(i) + "\n")


def recompose(file, N):
    with open(file) as f:
        data = [x.strip() for x in f.readlines()]
    k = 1
    l = 1
    for i in data:
        with open(f"File_{k}", "a") as file:
            file.write(f"{i}\n")
        
        if l % N == 0:
            k += 1
        l += 1
recompose("data.txt", 3)

def recomposee(path, N):
    with open(path) as f:
        data = [l.strip() for l in f]
    
    inlines = []
    n = 0
    for i in range(len(data) // N):
        if n + 2 * N <= len(data):
            inlines.append(data[n:n + N])
        else:
            
            inlines.append(data[n:n + N])
            l = []
            for j in range(n + N, len(data)):
                l.append(data[j])
            inlines.append(l)
        n += N
    k = 1
    for lines in inlines:
        for i in lines: 
            with open(f"splited {path}_{k}", "a") as f:
                f.write(f"{i}\n")
        k += 1

    return 0
recomposee("data.txt", 3)
