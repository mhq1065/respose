A = [1,5,6,9,15,19]
B = [2,3,6,13,15,33]
C = A + B
C = list(set(C))
C.sort()
print(C)