a=[]
N=int(input("请输入元素个数"))
for i in range(N):
    k=int(input("请输入第"+str(i)+"元素："))
    a.append(k)
for i in range(N-1,-1,-1):
    print(a[i],end=' ')
print()