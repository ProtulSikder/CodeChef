while 1:
    n = int(input())
    if n == 0:
        break
    
    s = list(map(int,input().split()))

    for i in range(1,n+1):
        pos = s.index(i)
        if s[i-1] != pos+1:
            print('not ambiguous')
            break
    else:
        print('ambiguous')
    
