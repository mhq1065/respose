def printlist(L):
    k=1
    for i in L:
        print(i,end='\t')
        if k%4==0:
            print()
        k=k+1
    print()
print("显示列表元素")
L=[1,2,3,4,5,6,7,8,9,10,11,12]
print(L)
print("程序结束")