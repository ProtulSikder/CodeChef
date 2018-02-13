t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    list_a = []
    for j in range(n):
        a = input()
        list_a.append(a)
    collusion = 0
    for j in range(n-1):
        for k in range(j+1,n):
            for p in range(m):
                if list_a[j][p] == '1' and list_a[k][p] == '1':
                    collusion += 1
    print(collusion)
