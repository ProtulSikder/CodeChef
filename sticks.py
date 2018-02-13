for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))

    my_li = set(s)
    set_s = list(my_li)
    set_s.sort(reverse=1)

    counts = []
    flag = 1
    
    for i in set_s:
        if s.count(i) >= 2:
            if s.count(i) >= 4 and len(counts) == 0:
                print(i*i)
                flag = 0
                break
            counts.append(i)
            if len(counts) == 2:
                break
    if flag:
        if len(counts) < 2:
            print(-1)
        else:
            print(counts[0]*counts[1])
