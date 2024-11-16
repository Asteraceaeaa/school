"""

    Задание №3
    Прочитать файл input.txt и создать новый файл output.txt, 
    в котором все буквы заменены на заглавные.

"""


with open("./files/Task-3/input.txt", "r") as input_data:
    data = input_data.read()
    upper_data = data.upper()

with open("./files/Task-3/output.txt", "w") as output:
    output.write(upper_data)