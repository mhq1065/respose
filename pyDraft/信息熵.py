from math import *
print("信息熵")
while True:
    n=int(input("个数"))
    a=[]
    sum1=0
    for i in range(n):
        k=float(input("数字"))
        a.append(k)
    for i in range(n):
        sum1=sum1-log(a[i]**2,2)
    print(sum1)
    print()
