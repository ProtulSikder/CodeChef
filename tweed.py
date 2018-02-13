t = int(input())

for i in range(t):
    n,p = input().split()

    a = list(map(int,input().split()))

    for j in a:
        if j % 2 == 1:
            b = 1
            break
        else:
            b = 0

    if p == 'Dee' and b == 0 and int(n) == 1 :
        print('Dee')

    else:
        print('Dum')
