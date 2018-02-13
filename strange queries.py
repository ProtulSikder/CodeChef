t = int(input())

for i in range(t):
    n,q = map(int,input().split())

    a = list(map(int,input().split()))

    for j in range(q):
        typ,x = map(int,input().split())

        sum = 0
        
        if typ == 1:
            a.append(x)

        else:
            a.remove(x)

        a.sort()
        if len(a) % 2 == 0:
            summ = 0
            for i in range(0,len(a)-1,2):
                summ += abs(a[i] - a[i+1])
        else:
            summ = abs(a[0]-a[1]) + abs(a[-1]-a[-2])
            for i in range(2,len(a)-2):
                if abs(a[i-1]-a[i]) <= abs(a[i]-a[i+1]):
                    summ += abs(a[i-1]-a[i])
                else:
                    summ += abs(a[i]-a[i+1])

        print(summ)
        
