A = list(map(int, input("Введите  координаты вершины A в формате x;y ").split(";")))
B = list(map(int, input("Введите  координаты вершины B в формате x;y ").split(";")))
C = list(map(int, input("Введите  координаты вершины C в формате x;y ").split(";")))

BC = ((C[0] - B[0]) ** 2 + (C[1] - B[1]) ** 2) ** 0.5
AC = ((C[0] - A[0]) ** 2 + (C[1] - A[1]) ** 2) ** 0.5
AB = ((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) ** 0.5

if BC + AC > AB and AC + AB > BC and BC + AB > AC:
    if AB == AC == BC:
        print("Треугольник существует и он равносторонний")
    elif AB == AC or AC == BC or BC == AB:
        print("Треугольник существует и он равнобедренный")
    else:
        print("Треугольник существует и он разносторонний")
else:
    print("Не существует")