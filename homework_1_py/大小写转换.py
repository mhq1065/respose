print("小写转大写")
s1=input("请输入一个字符串 ")
n=len(s1)
s2=""
for i in range(n):
    if s1[i]<='z'and s1[i]>='a':
        c=ord(s1[i])-32
        c=chr(c)
        s2=s2+c
    else:
        s2=s2+s1[i]
print(s2)
print("程序结束.")
