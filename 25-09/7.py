n = 100
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i % 10:
            p = i
            for k in range(1, 444):
                if p % 10 ** k:
                    break
                else:
                    p = i * 10**k
        else: print(i + j)
            
    print(p + j)
        
            
