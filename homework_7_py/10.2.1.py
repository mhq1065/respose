def rootfirst(a,k,n):
    global N
    if k==1:
        print(a[k],end="")
    elif a[k] != "":
        print("",a[k],end="")
        N += 1
    if 2*k<=n:
        rootfirst(a,2*k,n)
    if 2*k+1<=n:
        rootfirst(a,2*k+1,n)
a=['','A','B','C','D','E','','F','','','G','','','','H','I']
N=1
n=len(a)-1
print("先序遍历：")
rootfirst(a,1,n)
print("列表长度：",n,'实际节点个数',N)