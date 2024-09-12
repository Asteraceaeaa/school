day = int(input("Введите номер дня недели - "))

if day <= 7:
    if 6 <= day <= 7:
        print("Выходные")
    else:
        print("Будни")
else:
    print("Ошибка")

