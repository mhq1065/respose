from turtle import *
import time
def koch(t,x,x0):
    if x<=x0:
        t.forward(x)
    else:
        koch(t,int(x/3),x0)
        t.left(60)
        koch(t,int(x/3),x0)
        t.right(120)
        koch(t,int(x/3),x0)
        t.left(60)
        koch(t,int(x/3),x0)
#
x0 = int(input("请输入终止长度（200-10）："))
spd = int(input("请输入绘制速度（1-100）："))
t = Pen()
t.up()
t.backward(200)
t.down()
t.speed(spd)
koch(t,400,x0)
done()
