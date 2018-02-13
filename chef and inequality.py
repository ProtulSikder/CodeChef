t = int(input())

for i in range(t):
    a,b,c,d = map(int,input().split())

    x = [m for m in range(a,b+1)]
    y = [n for n in range(c,d+1)]

    sum = 0
    
    for j in x:
        for k in y:
            if j<k:
                sum += 1

    print(sum)
