for _ in range(int(input())):
    n = int(input())

    a = [[int(x) for x in input().split()]for i in range(n)]

    m = 1

    while m < 4:
        city = 0
        dis = 0

        for i in range(n):
            if a[i][1] == m:
                if a[i][2] > dis:
                    dis = a[i][2]
                    city = a[i][0]
                elif a[i][2] == dis:
                    if a[i][0] < city:
                        city = a[i][0]

        print(dis,city)
        m += 1
    
