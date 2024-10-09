from random import randint
s = []

for i in range(10):
    s.append(randint(0, 100))
print(f"List: {s}")
for i in range(-2, -len(s), -1):
    if s [i + 1] < s[i] > s[i - 1]:
        print("The last local maximum is", s[i])
        break

