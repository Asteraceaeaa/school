time = int(input("Enter the current hour - "))

if 1 <= time <= 24:
    if 5 <= time <= 11:
        print("Gmorning!")
    elif 12 <= time <= 17:
        print("Have a nice day!")
    elif  18 <= time <= 22:
        print("Have a good evening!")
    else:
        print("Good night!")
else:
    print("ERROR")