def _odd_():
    n=1
    while 1:
        n += 2
        yield n
def disvisible(n):
    return lambda x: x%n>0
def prime():
    yield 2
    it = _odd_()
    while 1:
        n= next(it)
        yield n
        it = filter(disvisible(n),it)

for n in prime():
    if n<1000:
        print(n,end=' ')
    else:
        break
