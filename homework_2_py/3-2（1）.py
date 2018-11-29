print("计算最大公因数。")
while True:
    a=int(input("请输入一个正整数："))
    b=int(input("请输入另一个正整数："))
    if a<=0 or b<=0:
        break
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    print("公因数为：",a)
print("程序结束。")