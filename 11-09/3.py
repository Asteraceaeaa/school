a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a + b > c and b + c > a and c + a > b:
    print("Triangle is exists")
else:
    print("Triangle isn't exists")