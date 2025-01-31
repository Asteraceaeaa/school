"""
    Исполнитель преобразует число на экране.

У исполнителя есть три команды, которые обозначены буквами.

A.  Вычесть 1.

B.  Умножить на 2.

C.  Умножить на 3.

Программа для исполнителя  — это последовательность команд. Например, программа BAC при исходном числе 2 последовательно получит числа 4, 3, 9. Сколько существует программ, которые преобразуют исходное число 3 в число 15 и при этом не содержат двух команд A подряд?
"""

def F(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return F(x - 1, y) + F(x * 2, y) + F(x * 2, y)

print(F(3, 15))
