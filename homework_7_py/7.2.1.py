def Bi(x):
    N = "."
    a = int(x)
    b = x-a
    while a!=0:
        N = str(a%2)+N
        a //= 2
    if a == 0:
        N = "0"+N
    for i in range(8):
        N = N+str(int(b*2))
        b = b*2-int(b*2)
        if b == 0:
            break
    return N
if __name__ == "__main__":    
    counter = 1
    while 1:
        a = float(input("输入"+str(counter)+":\n"))
        if a == 0:
            print("输出"+str(counter)+"：\n0B")
            break
        print("输出"+str(counter)+":\n"+Bi(a)+"B")
        counter += 1