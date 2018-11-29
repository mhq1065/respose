print("级数求和")
sumn=0
n=int(input("请输入一个正整数"))
while n>=1:
    sumn=sumn+1/n**2
    n=n-1
print("级数和为",sumn)
print()