def factor(n):
    y=1
    while n>0:
        y=y*n
        n=n-1
    return y
print("计算n！")
n=int(input("请输入n："))
f=factor(n)
print(n,"!=",f)
print("结束")