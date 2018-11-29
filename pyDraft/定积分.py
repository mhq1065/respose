import math as math
while True:
    fun = input("请输入一个需要积分的式子")
    m = float(input("请输入下限"))
    n = float(input("请输入上限"))
    while m>n:
        print("上下限错误")
        m = float(input("请输入下限"))
        n = float(input("请输入上限"))
    result = 0
    while m<n:
        x = m
        result += eval(fun)*0.0001
        m += 0.0001
    print(result)