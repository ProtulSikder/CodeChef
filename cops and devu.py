t = int(input())
for i in range(t):
    m,x,y = map(int,input().split())
    poho = list(map(int,input().split()))
    home = x*y
    a = set()
    for j in poho:
        if j - home <= 1:
            be = 1
        else:
            be = j - home
        if j + home >= 100:
            af = 100
        else:
            af = j + home
        a.update(i for i in range(be,af+1))
    print(100-len(a))
