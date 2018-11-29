
while True:    
    k=int(input("请输入一个正整数"))
    s=1
    n=1
    while s<=k:
        s=s+1/s
        n=n+1
    print("a",n,"=",s)
    print()