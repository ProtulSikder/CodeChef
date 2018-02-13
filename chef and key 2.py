t = int(input())

for i in range(t):
    x,y,c = map(int,input().split())

    m = 1
    sum = 0

    while m<=c:
        if c%m == 0:
            d = c/m
            if m<=x and d<=y:
                sum+=1
        m += 1

    print(sum)
