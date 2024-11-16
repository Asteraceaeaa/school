"""

    Задание №6

    Напишите программу, которая считывает текст из файла sessage.txt и шифрует его 
    с помощью простого шифра Цезаря (сдвиг каждой буквы на 3 позиции вправо). 
    Зашифрованный текст сохраните в файл encrypted_message.txt.

"""

with open("./files/Task-6/message.txt") as message, open("./files/Task-6/encrypted_message.txt", "w") as encrypted_message:
    msg = message.read()
    for i in range(len(msg) + 1):
        encrypted_message.write(msg[i - 3]) #Сдвиг вправо по индексу


"""
    Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Например, в шифре со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее. Шифр назван в честь римского полководца Гая Юлия Цезаря, использовавшего его для секретной переписки со своими генералами.
    (Определение с вики)



with open("./files/Task-6/message.txt") as message, open("./files/Task-6/encrypted_message.txt", "w") as encrypted_message:
    msg = message.read()
    for char in msg:
            if ord("a") <= ord(char.lower()) <= ord("z"): #It's a letter?
            encrypted_message.write(chr(ord(char) + 3)) 
        else:
            encrypted_message.write(char)


#Что делать если попадется x, y, z я не понял.
"""
