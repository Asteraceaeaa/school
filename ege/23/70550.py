"""
    Исполнитель преобразует число на экране. У исполнителя есть две команды, которые обозначены латинскими буквами:

    A.  Вычти 2.

    B.  Найди целую часть от деления на 2.

    Программа для исполнителя  — это последовательность команд.

    Сколько существует программ, для которых при исходном числе 38 результатом является число 2 и при этом траектория вычислений содержит число 16?
"""

from re import L


s = [x for x in range(100) ]
print(s)
def summ(a, b):
    return a + b


for i in range(len(s) - 1):
    g, b = s[i], s[i - 1]
    print(summ(g, b))