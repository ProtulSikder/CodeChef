t = int(input())

for i in range(t):
    x,y,c = map(int,input().split())
    sum = 0

    for m in range(1,x+1):
        for n in range(1,y+1):
            if m*n > c:
                break
            if m*n == c:
                sum += 1

    print(sum)
