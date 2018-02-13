t = int(input())

for i in range(t):
    c,d,l = map(int,input().split())
    if l%4 == 0 and l >= d*4 and (c+d)*4 >= l:
        a = 0
        if c > 2*d:
            a = c-2*d
        if l >= (a+d)*4:
            print('yes')
            continue
    print('no')
