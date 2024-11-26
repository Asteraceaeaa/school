"""
    https://inf-ege.sdamgia.ru/problem?id=47210
"""
from turtle import *
k = 10; speed(0); color("black", "red"); begin_fill()  

for i in range(7):
    forward(10 * k)
    right(120)
end_fill()