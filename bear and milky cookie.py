t = int(input())
for i in range(t):
    n = int(input())
    a = input().split()
    if len(a) == 1:
        if a[0] == 'milk':
            print('YES')
        else:
            print('NO')
    elif a[-1] == 'cookie':
        print('NO')
    else:
        for j in range(len(a)-1):
            if a[j] == 'cookie':
                if a[j+1] != 'milk':
                    print('NO')
                    break
        else:
            print('YES')
    
            
