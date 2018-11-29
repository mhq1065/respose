def fu(n,k):
    L=[]
    for i in range(1,n+1):
        m=float(input("请输入第"+str(k)+"个向量的第"+str(i)+"个元"))
        L.append(m)
    return L

n=int(input("请输入向量的元数"))
L1=fu(n,1)
print()
L2=fu(n,2)
s=0
for i in range(n):
    s=L1[i]*L2[i]+s
print(s)
print("程序结束") 