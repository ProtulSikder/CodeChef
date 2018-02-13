t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    print(n*(m-1) + m*(n-1))
