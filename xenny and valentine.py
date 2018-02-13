t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    xenny = 0
    yana = 0
    for j in range(n):
        if j%2 == 0:
            xenny += x[j]
        else:
            xenny += y[j]
    for j in range(n):
        if j%2 == 0:
            yana += y[j]
        else:
            yana += x[j]
    if xenny < yana:
        print(xenny)
    else:
        print(yana)
    
    
