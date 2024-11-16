"""

    Задание №2
    Есть файл data.txt, содержащий числа, разделенные пробелами. 
    Создайте программу, которая читает эти числа, отбирает только четные и записывает их в файл even_numbers.txt.

"""


with open("./files/Task-2/data.txt", 'r') as data:
    nums = data.read().strip()
    nums = [x for x in nums.split(" ") if int(x) % 2 == 0]

with open("./files/Task-2/even_numbers.txt", "w") as evens:
    for i in nums:
        evens.write(i + " ")