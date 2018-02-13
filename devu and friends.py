t = int(input())
for i in range(t):
    n = int(input())
    d = list(input().split())
    f = []

    for j in d:
        if j not in f:
            f.append(j)
    print(len(f))
