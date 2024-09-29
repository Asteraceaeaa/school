n = int(input("Enter tne num => "))
cnt = 0
if n % 2 == 0:
    for i in range(2, n + 1, 2):
        if n % i == 0:
            print(i)
            cnt+=1
if cnt == 0:
    print("Number haven't an even divisor")
