"""

    Задача №1

    Написать программу, которая читает файл text.txt 
    и подсчитывает количество символов, слов и строк в этом файле. Вывести результаты на экран.

"""


with open("./files/Task-1/text.txt", 'r') as f:
    data = f.read()
    #Chars
    chars = ['' for _ in data.strip()]
    print(f"Chars: {len(chars)}")
    #Lines
    lines = data.splitlines()
    print(f"Lines: {len(lines)}")
    #Words
    words = [x.strip('\n') for x in data.strip().split(" ") if x != '']
    print(f"Words: {len(words)}")

    # print(data)
    
