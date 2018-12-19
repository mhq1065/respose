words = ['traceback','define','identifier','valid','invalid','syntax','indent','unexpected','indices']
expla = ['追溯','定义','标识符','有效的','无效的','语法','缩进','以外的','下标index的复数形式']
def bubleSort(words,expla):#冒泡排序
    for i in range(len(words)-1):
        for j in range(len(words)-1-i):
            if words[j]>words[j+1]:
                words[j],words[j+1]=words[j+1],words[j]
                expla[j],expla[j+1]=expla[j+1],expla[j]
def insertSort(words,expla):#直插
    for i in range(1,len(words)):
        temp = words[i]
        j = i-1
        while j>=0 and temp<words[j]:
            words[j+1]=words[j]
            j -= 1
        words[j+1]=temp
#简排不写了
def found(L,key):#二分法查找
    low = 0
    heigh = len(L)-1
    while low<=heigh:
        mid = int((low+heigh)/2)
        if key<L[mid]:
            heigh = mid-1
        elif key ==L[mid]:
            return mid
        else:
            low = mid+1
    return None
def add(word,mean,L,M):#插入
    for i in range(len(L)):
        if L[i]>=word:
            L.insert(i,word)
            M.insert(i,mean)
            return
    L.insert(len(L),word)
    M.insert(len(L),mean)
def add2(word,mean,L,M):#插入 课本解法
    L.append(word)
    M.append(mean)
    j = len(L)-1
    while j>=1 and L[j-1]>L[j]:
        L[j],L[j-1] = L[j-1],L[j]
        M[j],M[j-1] = M[j-1],M[j]
        j -=1

bubleSort(words,expla)
print(words)
print(expla)
while 1:    
    word = str(input("请输入单词"))
    n=found(words,word)
    if n!=None:
        print("该单词的意思是",expla[n])
    else:
        print("没有该单词")
        mean=input("该单词的已加入字典，请输入它的词义  ")
        add(word,mean,words,expla)
