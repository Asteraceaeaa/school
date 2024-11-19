"""

    Задание №6

    Напишите программу, которая считывает текст из файла sessage.txt и шифрует его 
    с помощью простого шифра Цезаря (сдвиг каждой буквы на 3 позиции вправо). 
    Зашифрованный текст сохраните в файл encrypted_message.txt.

"""
"""
alph = [chr(l) for l in range(1072, 1104)]

def checker(l):
    alph = [chr(l) for l in range(1072, 1104)]
    i = alph.index(l) + 3
    
    #Проверка волиднойсти индекса
    if len(alph) - 1 < i:
        print(-abs(i - len(l)))
        return -abs(i - len(l)) + 3
    else:
        return i 



with open("./files/Task-6/message.txt") as message, open("./files/Task-6/encrypted_message.txt", "w") as encrypted_message:
    msg = message.read()
    encrypted_msg = ''
    for i in range(len(msg)):
        if msg[i] in alph:
            encrypted_msg += alph[checker(msg[i])]
        else:
            encrypted_msg += msg[i]
    encrypted_message.write(encrypted_msg)

"""

alph = [chr(l) for l in range(1103, 1071, -1)]
print(alph)

with open("./files/Task-6/message.txt") as message, open("./files/Task-6/encrypted_message.txt", "w") as encrypted_message:
    msg = message.read()
    encrypted_msg = ''
    for i in range(len(msg)):
        if msg[i] in alph:
            encrypted_msg += alph[alph.index(msg[i]) - 3]
        else:
            encrypted_msg += msg[i]
    encrypted_message.write(encrypted_msg)