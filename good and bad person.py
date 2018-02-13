for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()

    small = sum(1 for c in s if c.islower())
    big = sum(1 for c in s if c.isupper())

    if big <= k and small <= k:
        print('both')
    elif small > big and big <= k:
        print('chef')
    elif big > small and small <= k:
        print('brother')
    elif big > k and small > k:
        print('none')
