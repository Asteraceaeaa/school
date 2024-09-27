n = int(input("Введите n => "))
a = int(input("Введите a => "))
r = int(input("Введите r => "))

for i in range(0, n + 1):
    print(f"{i + 1} Член = {a * r ** i}")
