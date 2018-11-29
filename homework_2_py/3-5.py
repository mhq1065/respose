a=[9,34,7,26,20,16,24,149,40,41]
while True:
    k=int(input("请输入一个数"))
    time=1
    i=0
    for i in a:
        if i==k:
            break
        time=time+1
    if time>len(a):
        print("不存在")
    else:
        print("找到了，找了",+time,"次",sep='')