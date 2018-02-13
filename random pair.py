t = int(input())

for i in range(t):
    n = int(input())

    a = list(map(int,input().split()))

    prob_1 = a.count(max(a))/len(a)

    a.remove(max(a))

    prob_2 = a.count(max(a))/len(a)

    print()
