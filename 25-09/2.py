n = int(input("Введите n => "))
a = int(input("Введите a => "))
r = int(input("Введите r => "))

for i in range(1, n + 1):
    print(f"{i} Член = {a * r ** (i - 1)}")
