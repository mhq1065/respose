print("这是一个复杂分段函数")
t=float(input("请输入一个值："))
if (t>30 or t<0):
    print("无定义")
else:
    if (t<5):
        y=t+10
    else:
        if (t<10):
            y=3*t
        else:
            if (t<20):
                y=30
            else:
                y=-3*t+90
    print("函数的值为：",y)
