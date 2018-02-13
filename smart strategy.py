t = int(input())

for i in range(t):
    n,q = map(int,input().split())

    d = list(map(int,input().split()))

    x = list(map(int,input().split()))

    mul_d = 1
    
    for j in d:
        mul_d *= j

    for j in x:
        print(j//mul_d,end=' ')

    print('')
