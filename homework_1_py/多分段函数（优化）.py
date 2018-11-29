print("这是一个玩具")
t=float(input("你想输入啥就输入啥"))
if t>30 or t<0:
    print("不存在的")
elif t<5:
    y=t+10
elif t<10:
    y=3*t
elif t<20:
    y=30
else:
    y=-3*t+10
if t<=30 and t>=0:
    print("函数值为：",y)
