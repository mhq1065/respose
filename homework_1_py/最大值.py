def max2(a,b):
    if a>=b:
        return a
    else:
        return b
def max3(a,b,c):
    return max2(max2(a,b),c)
print("求最大值")
a=float(input("请输入第1个数"))
b=float(input("请输入第2个数"))
c=float(input("请输入第3个数"))
print("最大值为",max3(a,b,c))