n = 10
P = int(input("Введите объем населения (чел) => "))
r = int(input("Процент => "))

for i in range(n):
    P *= r / 100 + 1
print("Через n лет население будет составлять", round(P), "человек")