for _ in range(int(input())):
    n = int(input())
    a = [[int(i)for i in input().split()]for j in range(n)]
    last = max(a[-1])
    summ = last
    if n < 2:
        print(summ)
        continue
    for i in range(n-2,-1,-1):
        while len(a[i])>0:
            c = max(a[i])
            if c < last:
                summ += c
                last = c
                break
            else:
                a[i].remove(c)
        else:
            print(-1)
            break
    else:
        print(summ)
            
