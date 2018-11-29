def make(n):
    sumn=0
    while n>=1:
        sumn=sumn+n
        n=n-1
    return sumn
print("数列求和")
while True:
    n=int(input("请输入一个正整数"))
    print("结果为",make(n))
print()
