for _ in range(int(input())):
    n = int(input())

    a = []

    for i in range(1,200,2):
        a.append(i)
        if len(a) == n:
            break
    print(' '.join(str(i) for i in a))
