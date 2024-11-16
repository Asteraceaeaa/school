"""

    Задание №2
    
    Есть файл data.txt, содержащий числа, разделенные пробелами. 
    Создайте программу, которая читает эти числа, отбирает только четные и записывает их в файл even_numbers.txt.

"""

"""
#Generate data
from random import randint

with open("./files/Task-2/data.txt", 'w') as f:
    for _ in range(100):
        f.write(f"{randint(0, 100)} ")
"""


with open("./files/Task-2/data.txt", 'r') as data:
    nums = data.read().strip()
    # print(nums)
    even_nums = [x for x in nums.split(" ") if int(x) % 2 == 0]

with open("./files/Task-2/even_numbers.txt", "w") as evens:
    for i in even_nums:
        evens.write(i + " ")