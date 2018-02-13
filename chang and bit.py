t = int(input())

for i in range(t):
    n = int(input())

    a = list(map(int,input().split()))
    cost = 0
    for j in a:
        cost = cost|j

    print(cost)
