t = int(input())
for i in range(t):
    n = input()
    if '1' in n:
        a = n.replace('0',' ')
        b = a.strip()
        if ' ' in b:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')
    
