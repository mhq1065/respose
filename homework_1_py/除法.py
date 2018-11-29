print("计算除法")
while True:
    a=float(input("请输入被除数a="))
    b=float(input("请输入除数b="))
    if a!=0 and b==0:
        continue
    if a==0 and b==0:
        break
    c=a/b
    print("商为：",c)
print("程序结束")
