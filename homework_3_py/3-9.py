a=int(input("请输入一个正整数"))
m=0
for i in range(len(str(a))):
    m=a%10+m*10
    a=int(a/10)
print(m)