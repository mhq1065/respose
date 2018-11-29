from math import *
print("分段函数的运算")
x=float(input("请输入自变量x的值："))
if x<=2 or x>5:
    y=x**2+2
else:
    y=2*x
print("函数的值为：",y)
