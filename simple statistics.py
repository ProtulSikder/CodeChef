'''for _ in range(int(input())):
    n,k = map(int,input().split())

    s = list(map(int,input().split()))

    for i in range(k):
        s.remove(max(s))
        s.remove(min(s))

    print('%.6f'%(sum(s)/len(s)))'''

for _ in range(int(input())):
    n,k = map(int,input().split())

    s = list(map(int,input().split()))

    s.sort()

    if k > 0:
        a = s[k:-k]
        print('%.6f'%(sum(a)/len(a)))
    else:
        print('%.6f'%(sum(s)/len(s)))
