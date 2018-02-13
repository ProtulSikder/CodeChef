t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    if a + 2 == b or b + 2 == a:
        print('YES')
        continue
    if a > 2:
        if a - 2 == b:
            print('YES')
            continue
    if b > 2:
        if b - 2 == a:
            print('YES')
            continue
    if a%2 == 1:
        if a + 1 == b:
            print('YES')
            continue
    if a%2 == 0:
        if a -1 == b:
            print('YES')
            continue
    if b%2 == 1:
        if b + 1 == a:
            print('YES')
            continue
    if b%2 == 0:
        if b - 1 == a:
            print('YES')
            continue
    print('NO')
