N = 0
def LDR(a,k,n):
    global N
    if 2*k<=n:
        LDR(a,2*k,n)
    if a[k] != "" and N==0:
        print(a[k],end="")
        N += 1
    elif a[k] != "":
        print("",a[k],end="")
        N += 1
    if 2*k+1<=n:
        LDR(a,2*k+1,n)
def DLR(a,k,n):
    if k==1:
        print(a[k],end="")
    elif a[k] != "":
        print("",a[k],end="")
    if 2*k<=n:
        DLR(a,2*k,n)
    if 2*k+1<=n:
        DLR(a,2*k+1,n)
def LRD(a,k,n):
    global N
    if 2*k<=n:
        LRD(a,2*k,n)
    if 2*k+1<=n:
        LRD(a,2*k+1,n)
    if a[k] != "" and N==0:
        print(a[k],end="")
        N += 1
    elif a[k] != "":
        print("",a[k],end="")
        N += 1
a=['','A','B','C','D','','E','F','G','H','','','I','J','K','L']
N=0
n=len(a)-1
print("中序遍历：")
LDR(a,1,n)
print()
print("先序遍历：")
DLR(a,1,n)
print()
N = 0
print("后序遍历：")
LRD(a,1,n)
