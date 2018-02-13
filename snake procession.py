import re
r = int(input())

for i in range(r):
    l = int(input())
    s = input()
    a = s.replace('.','')
    
    if len(a) > 0:
        if a[0] != 'H':
            print('Invalid')

        else:
            num = re.findall('HT',a)

            if len(num)*2 == len(a):
                print('Valid')
            else:
                print('Invalid')

    else:
        print('Valid')

    
