from multiprocessing.reduction import _ForkingPickler
import os


#1
with open("data.txt", "w") as f:
    user_input = input()
    f.write(user_input)


#2

with open("user_outpu.txt", "a") as f:
    user_input = input()
    while user_input != '':
        f.write(user_input + "\n")
        user_input = input()

#3 + #4
path = input("Enter the path => ")

with open(path) as f:

    i = 1
    for line in f:
        print(f"{i} {line}")
        i += 1
# print(os.path.join("/home/asteracea/Documents/school/school/lessons/09-12-24", "add"))
def app(path, N):
    path_ = "/home/asteracea/Documents/school/school/lessons/09-12-24"
    with open(os.path.join(path_, file)) as file:
        file = [a for a in file.readlines()]
        c = 0
        p = 1; i = 0
        while i != len(f) + 1:
            f = open(os.path.join(path_, f"part-{p}"), "a")
            f.append(f"{f[i]} \n")
            f.close()
            c += 1; i += 1
            if N <= c:
                p += 1
                c = 0
                
                
                
            
