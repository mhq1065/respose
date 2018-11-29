import re
def demo(a):
    b=''
    for i in range(len(a)-1):
        b += str(9-int(a[i]))
    b += str(10-int(a[-1]))
    return b
while 1:
    number = input("Please input the number:")
    paterm1 = re.compile('^[+]?[0-9]+\.[0-9]+$')
    paterm2 = re.compile('^[+-]?[0-9]+$')
    paterm3 = re.compile('^[-][0-9]+\.[0-9]+$')
    result1 = paterm1.match(number)
    result2 = paterm2.match(number)
    result3 = paterm3.match(number)
    if result1:
        print('0'+number[number.find('.'):])
    elif result2:
        print(0)
    elif result3:
        print(r'0.'+demo(number[number.find('.')+1:]))
    else:
        print ("非法输入")