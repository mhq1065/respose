def De(x):
    N = 0
    i = 0
    while i<len(x) and x[i] != '.':
        N=N*2+ord(x[i])-ord('0')
        i += 1
    i += 1
    weight = 0.5
    while i<len(x):
        N += (ord(x[i])-ord('0'))*weight
        weight /= 2
        i += 1
    return N
counter = 1
while True:
    a = input("输入"+str(counter)+"：")
    if float(a) == 0:
        print("输出"+str(counter)+"：0")
        break
    print("输出"+str(counter)+"："+str(De(a)))
    counter += 1