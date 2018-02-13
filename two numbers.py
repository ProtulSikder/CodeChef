for _ in range(int(input())):
    a,b,n = map(int,input().split())
    if n%2 == 0:
        a *= 2**(n//2)
        b *= 2**(n//2)
    else:
        a *= 2**((n+1)//2)
        b *= 2**((n-1)//2)
    print(max(a,b)//min(a,b))
