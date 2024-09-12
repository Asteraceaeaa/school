A = list(map(int, input("Enter A(x1;y1) here (in format: x;y) => ").split(";")))#Initial point; A[0] = x1; A[1] = y1
B = list(map(int, input("Enter B(x2;y2) here (in format: x;y) => ").split(";")))#End point; B[0] = x1; B[1] = y1

if (8 >= A[0] > 0) and (8 >= A[1] > 0) and (8 >= B[0] > 0) and (8 >= B[1] > 0):
    if abs(A[0] - B[0]) == 2 and abs(A[1] - B[1]) == 1 or abs(A[0] - B[0]) == 1 and abs(A[1] - B[1]) == 2:
        print("Konyaka doskakal")
    else:
        print("eto ne konyaka")

else:
    print("Coordinates is not valid")

"""
#autotest
def solution(A, B):
    if (8 >= A[0] > 0) and (8 >= A[1] > 0) and (8 >= B[0] > 0) and (8 >= B[1] > 0):
        if abs(A[0] - B[0]) == 2 and abs(A[1] - B[1]) == 1 or abs(A[0] - B[0]) == 1 and abs(A[1] - B[1]) == 2:
            print("Konyaka doskakal")
        else:
            print("eto ne konyaka")

    else:
     print("Coordinates is not valid")

solution([1,1], [2,2]) #NO
solution([1,1], [3,2]) #YES
solution([3,8], [2,6]) #YES
solution([3,4], [5,6]) #NO
"""



