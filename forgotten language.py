for _ in range(int(input())):
    n,k = map(int,input().split())
    f_lan = input().split()
    all_lan = []
    for i in range(k):
        k_lan = input().split()
        for j in range(1,len(k_lan)):
            all_lan.append(k_lan[j])
    for i in f_lan:
        if i in all_lan:
            print('YES',end=' ')
        else:
            print('NO',end=' ')
    print()
