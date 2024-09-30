money = 10000; sale = 1
cost = int(input("Enter rhe initial cost => "))
sale_increase = int(input("Enter the sale increment => "))
cnt = 0
for i in range(money **     print(i)
    if (money - cost) >= 0:
        money -= cost
        
    else:
        cnt = i
        break
    cost = cost // sale - (sale_increase / 100)
print(f"Money remains: {round(money, 2)}, count of goods: {cnt}")
    
