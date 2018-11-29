print("这是一个计算最大值最小值平均值的程序")
L=[17,38,20,16,3,24,30,44,-10,12]
N=len(L)
minl=L[0]
maxl=L[0]
suml=L[0]
for i in range (1,N):
    if minl>L[i]:
            minl=L[i]
    if maxl<L[i]:
            maxl=L[i]
    suml=suml+L[i]
ave=suml/N
print("最大",maxl,"最小",minl,"平均",ave)
        
