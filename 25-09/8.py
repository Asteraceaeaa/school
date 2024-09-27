cnt = int(input())
time = 0

for i in range(cnt):
    l = int(input(f"Enter the length of the {i + 1} region => "))
    avg_speed = int(input("Enter the avg speed of the {i + 1} region => "))
    time += l / avg_speed

print(f"Overage time of the movement: {time}")
