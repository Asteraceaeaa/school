stipendia = 22000; rashodi = 24000
# initial_sum = mounths * (rashodi - stipendia)
rashodi_with_inflation = 24000; base_inflation = 1.03
mounths = 12

first = 0; secnd = 0

for mounth in range(1, mounths + 1):
    first += rashodi - stipendia
    secnd += rashodi_with_inflation - stipendia

    if (mounth + 1) % 2 == 1: #С учетом того, что в первый месяц повышение цен отстуствует
        rashodi_with_inflation *= base_inflation
    else:
        rashodi_with_inflation *= base_inflation + .02
print(f"3.1: {first} \n3.2: {secnd}")


