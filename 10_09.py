#Нужно найти периметр и площадь треугольника по координатам вершин

def solution(A, B, C):
    #Находим длины сторон
    AB = ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5
    BC = ((B[0] - C[0]) ** 2 + (B[1] - C[1]) ** 2) ** 0.5
    AC = ((C[0] - A[0]) ** 2 + (C[1] - A[1]) ** 2) ** 0.5
    #Находим периметр
    P = AB + BC + AC
    #Находим площадь по формуле Герона
    p = P / 2
    S = (p * (p - AB) * (p - BC) * (p - AC)) ** 0.5

    return{
        "Периметр": P,
        "Площадь": S,
    }

A = list(map(int, input("A(x; y): ").split(";")))
B = list(map(int, input("B(x; y): ").split(";")))
C = list(map(int, input("C(x; y): ").split(";")))

print(solution(A, B, C))