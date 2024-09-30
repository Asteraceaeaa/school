n = int(input("Enter n: "))
summ = 0
product = 1
for i in range(1, n + 1):
    summ += i
    product *= i
    
print(f"The product of numbers for 1 to {n} = {product}, the sum of numbers = {summ}, avg: {summ / n}")
