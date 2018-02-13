for _ in range(int(input())):
    n = input()
    a = list(map(int,input().split()))

    if 2 in a:
        print('No')
        continue
    else:
        if 5 not in a:
            print('No')
            continue
        else:
            avg = sum(a)/int(n)

            if avg < 4:
                print('No')
                continue
            else:
                print('Yes')
            
