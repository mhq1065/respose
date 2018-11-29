def gys(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
print("这是一个计算最大公因数的程序")
while True:
    a=int(input("请输入一个正整数："))
    b=int(input("请输入令一个正整数："))
    print("最大公因数为：",gys(a,b))