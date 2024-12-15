
"""
    Текстовый файл состоит из цифр от 1 до 6, знаков операций «—» и «*» (вычитание и умножение) и заглавных латинских букв A, B, C, D.

    Определите максимальное количество символов в непрерывной последовательности символов, состоящей из буквы В, за которой следует корректное арифметическое выражение с целыми неотрицательными числами, записанными в десятичной системе счисления.


"""


with open("/home/asteracea/Documents/school/school/ege/24/72609.txt") as f:
    f = [ a for a in f.read()]
    # print(f)
mc = 0
letters = ["A", "B", "C"]
operands = ["-", "*"]


for i in range(len(f)):
    c = 0
    while f[i] == "B":
        c += 1
        i += 1
    i += 1


    if c > mc:
        
        res = False
        
        while f[i] not in letters:
            if f[i] in operands:
                if f[i + 1] in letters and f[i + 1] not in operands:
                    res = False
                    break
                else:
                    res = True
            i += 1
        