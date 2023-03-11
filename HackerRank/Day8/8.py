x = { k : v for k, v in (input('Enter name and number: ').split() for _ in range(int(input('Enter count of elements: ')))) }
#x = {'sam': '99912222', 'tom': '11122222', 'harry': '12299933'}

while True:
    try:
        y = input('Enter finding names: ')
        #y = ('sam','edward','harry')
    except EOFError:
        break
    if y in x.keys():
        print('{}={}'.format(y,x[y]))
    else:
        print('Not found')


