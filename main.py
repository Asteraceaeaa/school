# Задача 1
# Напишите программу, которая предлагает ввести два целых числа,
# а затем использует конструкцию if-else для вывода сообщения о том,
# равны ли два числа.

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if first == second:
    print(f'First num equal Second num: {first} = {second}')
else:
    print(f'First num not equal Second num: {first} != {second}')



