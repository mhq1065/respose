def search(L,key):
    n = 0
    for i in L:
        if i == key:
            return n
        n += 1
    return -1
#程序
while 1: 
    L1 = [12,14,134,21,4,124,112,41,2,3412,34,1243]
    key = int(input("待查找的数是："))
    n = search(L1,key)
    if n == -1:
        print("没找到")
    else:
        print(key,"是下标为%d的元素" %n)
