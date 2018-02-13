for _ in range(int(input())):
    rows = int(input())
    a = []

    for i in range(rows):
        b = [int(j) for j in input().split()]
        a.append(b)

    for i in range(rows-1,0,-1):
        for j in range(i):
            if a[i][j] > a[i][j+1]:
                a[i-1][j] += a[i][j]
            else:
                a[i-1][j] += a[i][j+1]
    print(a[0][0])
