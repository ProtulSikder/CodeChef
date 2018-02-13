for _ in range(int(input())):
    a = list(map(int,input().split()))
    c = [i for i in a]
    b = []
    for i in range(3):
        b.append(min(c))
        c.remove(min(c))
    if sum(b) < max(a):
        print('NO')
        continue
    for i in a:
        if a.count(i) != 2:
            print('NO')
            break
    else:
        print('YES')
