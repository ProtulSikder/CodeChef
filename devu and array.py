n,q = map(int,input().split())

my_list = list(map(int,input().split()))

mn = min(my_list)
mx = max(my_list)

for _ in range(q):
    t = int(input())

    if len(my_list) == 1:
        if t == my_list[0]:
            print('Yes')
        else:
            print('No')
    else:
        if t >= mn and t <= mx:
            print('Yes')
        else:
            print('No')
