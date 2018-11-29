a=input("输入：\n")
N=0
for i in a:
    N = N*2 + ord(i) - ord('0')
print("输出：\n"+str(N))