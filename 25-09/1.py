n = int(input())

"""
Нашел в интернете
def is_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    head, tail = x, 0
    while head > tail:
        head, tail = head // 10, tail * 10 + head % 10
    # When the length is an odd number, we can get rid of the middle digit by tail // 10
    return head == tail or head == tail // 10
    
    #https://stackoverflow.com/questions/50660606/check-if-a-number-is-a-palindrome-without-changing-it-into-string#:~:text=def%20is_palindrome(x,or%20head%20%3D%3D%20tail%20//%2010
"""

for i in range(100, n + 1):
    if i % 10 != 0:
        head, tail = i, 0
        for j in range(i):
            if head > tail:
                head, tail = head // 10, tail * 10 + head % 10
            else: break
        if head == tail or head == tail // 10:
            print(i)


# n = 10000
# def length(n):
#     prev = 0
#     for i in range(2, 1000):
#         this = n % 10 ** (i + 1)
#         if prev == this:
#             length = i
#             break
#         else:
#             prev = this
#
#     return length
#
# for i in range(100, n + 1):
#     for j in range(2, length(i) + 1):
#         print(j)
