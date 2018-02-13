t = int(input())
for i in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    print(num.index(min(num))+1)
