#k = tgAlpha
#b - точка пересечения прямой с осью ординат

A = list(map(int, input().split(";")))
B = list(map(int, input().split(";")))

C = [max(A[0], B[0]), min(A[1], B[1])]
tgAlpha = ((C[0] - B[0]) ** 2 + (C[1] - B[1]) ** 2) ** 0.5 / ((C[0] - A[0]) ** 2 + (C[1] - A[1]) ** 2) ** 0.5
print(A, B, C)
print(tgAlpha)
