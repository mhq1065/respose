H="0123456789ABCDEF"
a=int(input("输入：\n"))
N=""
while a!=0:
    N=H[a%16]+N
    a //= 16
print("输出：\n"+N)