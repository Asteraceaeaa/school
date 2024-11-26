#7.1

def is_prime(n):
    
    res = 0
    for i in range(2, n):
        if res > 0:
            return "is not prime"
        if n % i == 0:
            res += 1

    return "is prime"

        
print(is_prime(7))

#7.2
#Здравствуйте, Иван!
#Привет, Мария!