print("这是一个计算pai的程序")
while True:
    pai=2
    n=int(input("请输入一个正整数"))
    for i in range(1,n+1):
        pai=pai*(2*i)*(2*i)/(2*i-1)/(2*i+1)
    print(pai)
    print()