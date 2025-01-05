conditions = [False for _ in range(4)]
symbols = [s for s in "!@#$%^&*()/"]

while False in conditions:
    password = input()
    
    conditions = [any(l.isdigit() for l in password),
                  any(l.islower() for l in password),
                  any(l.isupper() for l in password),
                  not any(l.isspace() for l in password),
                  any(l in symbols for l in password),
                  not " " in password,
                  len(password) >= 8
                  ]
    
    print("Пароль должен содержать заглавные и строчные буквы, цифры, пробелы и специальные символы.\nИ быть не менее 8 символов в длину. \nА также не содержать пробелов ")
    
print(f"Пароль {password} одобрен")
 


