"""

    Задание №4

    Напишите программу, которая открывает файл story.txt, 
    находит в тексте все вхождения слова "Python" и заменяет их на "Java". 
    Результат сохраните в новый файл new-story.txt.

"""

with open("./files/Task-4/story.txt", "r") as f:
    new = f.read().strip().replace("Python", "Java")
    new_f = open("./files/Task-4/new-story.txt", "w") 
    new_f.write(new)
    new_f.close()



