for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    money = list(map(int,input().split()))

    c = 0
    
    for i in range(n):
        if a[i] == b[i]:
            c += 1
    if c == n:
        print(money[-1])
    else:
        print(max(money[:c+1]))
