t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    if sum(arr) % 2 == 0:
        if k == 1:
            print('odd')
        else:
            print('even')
    else:
        print('even')
