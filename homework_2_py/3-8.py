def transform(k):
    n=ord(k)
    if n>=65 and n<=90:
        return chr(n+32)
    elif n>=97 and n<=122:
        return chr(n-32)
    else:
        return chr(n)
print("大小写转换")
while True:
    s1=input("请输入字符串")
    long=len(s1)
    s2=""
    for i in range (long):
        s2=s2+transform(s1[i])
    print(s2)
