
 = 10
exchange_rate = int(input("Enter initial exchange rate: "))
change_rate = int(input("Enter percentage of changes in %(from 1 to 100): "))

for i in range(1, n + 1):
    print(f"Exchange rate in {i} day: {round(exchange_rate, 3)}$")
    exchange_rate *= change_rate / 100 + 1
