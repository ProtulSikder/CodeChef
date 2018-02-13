t = int(input())

for i in range(t):
    n = int(input())

    c = list(map(int,input().split()))
    sorted_c = sorted(c)
    
    check = 0

    for j in range(n):
        if c[j] != sorted_c[j]:
            check = 1
            break
    for j in range(n):
        if sorted_c[j] != j+1:
            check = 0
            break

    if check == 1:
        print('yes')

    else:
        print('no')

    
