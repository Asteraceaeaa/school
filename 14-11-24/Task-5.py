"""

    Задание №3

    У вас есть два файла part1.txt и part2.txt.
    Напишите программу, которая объединяет содержимое этих файлов и сохраняет в новый файл fulltext.txt.
"""

with open("./files/Task-5/part1.txt") as p1, open("./files/Task-5/part2.txt") as p2, open("./files/Task-5/fulltext.txt", "w") as full:
    part1 = p1.read()
    part2 = p2.read()
    full.write(part1 + part2)


