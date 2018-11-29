A = ['小明','小红','小兰']
n = input('请输入学生姓名')
for i in A:
    if i==n:
        print(A.index(i))
    else:
        continue