t = int(input())

for i in range(t):
    n = int(input())

    s = list(map(int,input().split()))

    maxi = max(s)

    be_sub = [j for j in range(1,maxi)]
    af_sub = be_sub[::-1]

    main_s = be_sub + [maxi] + af_sub

    if main_s == s:
        print('yes')
    else:
        print('no')
    
    
