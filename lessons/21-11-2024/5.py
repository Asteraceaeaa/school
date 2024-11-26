#5.1
glasn = ["а", "у", "о", "э", "ы", "ю", "е", "я", "и"]
stroka = input("Enter something => ")
c = 0

for i in stroka:
    if i.lower() in glasn:
        c += 1
print(f"Glasnih: {c}")

#5.2
#hello, world!
#HELLO, WORLD!

