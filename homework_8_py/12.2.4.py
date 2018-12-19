def maxn(List):
    if len(List)==1:
        return List[0]
    else:
        if maxn(List[1:])>List[0]:
            return maxn(List[1:])
        else:
            return List[0]

a = [2,43,54,54,254,51,1,334,34,2,34,4,515,51]
print(maxn(a))