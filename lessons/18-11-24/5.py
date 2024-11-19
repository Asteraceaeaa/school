
with open("./files/names.txt") as names, open("./files/sorted_names.txt", "w") as s_names:
    names_l = [name.strip() for name in names.readlines()]
    names_l.sort()
    s_names.write("\n".join(names_l))


