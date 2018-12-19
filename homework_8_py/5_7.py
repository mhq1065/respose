information = [
    {
        'name':'郑志豪',
        'xuehao':'123456',
        'science':300,
        'English':100,
        'Math':100,
    },
    {
        'name':'wyk',
        'xuehao':'123457',
        'science':100,
        'English':200,
        'Math':100,
    },
    {
        'name':'wyz',
        'xuehao':'123458',
        'science':100,
        'English':100,
        'Math':200,
    },
    {
        'name':'许鑫凯',
        'xuehao':'123459',
        'science':1000,
        'English':1000,
        'Math':1000,
    },
]

m=sorted(information,key=lambda x : (x['Math']+x['English']+x['science'])/3,reverse=True)
print([i['name'] for i in m])