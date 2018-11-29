def mis(x,N):
    Dic = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = int(x)
    b = x - a
    result1 = []
    result2 = []
    result = ""
    while a != 0:
        result1.append(Dic[a%N])
        a //= N
    for i in range(16):
        if b==0:
            break
        result2.append(Dic[int(b*N)])
        b = b*N-int(b*N)
    if len(result1) == 0:
        result += '0'
    else:
        for i in range(len(result1)):
            result += result1.pop()
    if len(result2) != 0:
        result += '.' 
    for i in range(len(result2)):
        result += result2.pop(0)
    return result
while True:
    a=float(input("输入：\n"))
    b=int(input())
    print("输出")
    print(mis(a,b))