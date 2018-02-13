for _ in range(int(input())):
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,k+1):
        ans = max(ans,n%i)
    print(ans)
