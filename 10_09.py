A = list(map(int, input("A(x; y): ").split(";")))
B = list(map(int, input("B(x; y): ").split(";")))
C = list(map(int, input("C(x; y): ").split(";")))

def solution(A, B, C):
    AB = ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5
    BC = ((B[0] - C[0]) ** 2 + (B[1] - C[1]) ** 2) ** 0.5
    AC = ((C[0] - A[0]) ** 2 + (C[1] - A[1]) ** 2) ** 0.5

    P = AB + BC + AC
    p = P / 2
    S = (p * (p - AB) * (p - BC) * (p - AC)) ** 0.5

    return{
        "Периметр": P,
        "Площадь": S,
    }

print(solution(A, B, C))