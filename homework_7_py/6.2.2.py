a=int(input("输入：\n"))
N=""
while a!=0:
    N=str(a%2)+N
    a=a//2
print(N)