L1=[]
n=int(input("请输入向量的元数"))
for i in range(1,n+1):
    m=float(input("请输入第一个向量的第"+str(i)+"个元"))
    L1.append(m)

L2=[]
for i in range(1,n+1):
    m=float(input("请输入第二个向量的第"+str(i)+"个元"))
    L2.append(m)

s=0
for i in range(n):
    s=L1[i]*L2[i]+s

print(s)