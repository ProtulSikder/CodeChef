for _ in range(int(input())):
    n,b,m = map(int,input().split())

    time = 0

    while n > 0:
        if n % 2 == 0:
            i = n // 2
        else:
            i = (n+1) // 2

        time += i * m
        
        m *= 2

        n -= i

        if n != 0:
            time += b

    print(time)
        
