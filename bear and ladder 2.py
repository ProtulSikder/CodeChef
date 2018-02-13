t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    if a > b:
        a,b = b,a
    if a + 2 == b:
        print('YES')
        continue
    if a % 2 == 1 and a + 1 == b:
        print('YES')
        continue
    print('NO')
