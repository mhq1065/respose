def hanoi(n,chA,chB,chC):
    global N
    if n==1:
        print(chA,"->",chC)
        N += 1
    else:
        hanoi(n-1,chA,chC,chB)
        print(chA,"->",chC)
        N += 1
        hanoi(n-1,chB,chA,chC)

N=0
print("本程序显示Hanoi问题的求解过程")
n = int(input("请输入盘子数n:"))
if n<1:
    n=1
y = hanoi(n,'A','B','C')
print("移动次数为：",N)