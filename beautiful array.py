t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    zero = 0
    minus_one = 0
    one = 0
    others = 0
    for j in arr:
        if j == 0:
            zero += 1
        elif j == -1:
            minus_one += 1
        elif j == 1:
            one += 1
        else:
            others += 1
    if others > 1:
        print('no')
        continue
    if minus_one == 1 and others == 1:
        print('no')
        continue
    if zero > 1 and 
