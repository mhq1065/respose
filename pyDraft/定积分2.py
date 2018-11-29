import numpy as np
from math import *
print("如果需要输入pi，请输入较多位数以保证精度")
print("*尚未补充安全监测")
while True:
    fun = input("请输入一个需要积分的式子")
    m = float(input("请输入下限"))
    n = float(input("请输入上限"))
    if m>n:
        m = m + n
        n = m - n
        m = m - n
        a = 1
    else:
        a = 0
    result = 0
    lin = list(np.linspace(m,n,2))
    space = (n-m)
    for i in lin:
        x = i
        g = 0
        exec('g='+fun+'*space')
        result += g
    if a==1:
        print(-1*result)
    else:
        print(result)