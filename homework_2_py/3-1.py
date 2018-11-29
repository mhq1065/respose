from math import *
print("这是一个计算分段函数的程序")
while True:
    x=float(input("请输入一个数"))
    y=(x+1)**2
    if x>=1:
        y=4-sqrt(x-1)
    print("函数值为",y)
print()
