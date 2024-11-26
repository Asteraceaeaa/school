with open("37368.txt") as ns:
    nums = [int(num.strip()) for num in ns.readlines() if int(num.strip()) % 2 == 0]  
    print(len(nums))

pars = []
sums = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        # print(j, end=";")
        a, b = int(nums[i]), int(nums[j])
        summ = a + b
        if summ % 60 == 0 and (a % 40 == 0 or b % 40 == 0):     
            pars.append([a, b])
            sums.append(summ)

print(max(sums), len(pars))     