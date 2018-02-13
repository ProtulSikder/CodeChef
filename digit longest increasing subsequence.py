t = int(input())

for i in range(t):
    n = int(input())

    lis = list(map(int,input().split()))

    new_lis = [str(j) for j in lis]

    print(''.join(new_lis))
