L=["month","Janurary","February","March","April","May","June","July","August","September","October","November","December"]
n=int(input("请输入一个月份"))
if n>=1 and n<=12:
    print(L[n])
else:
    print("不存在")