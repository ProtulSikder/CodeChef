import itertools

n, k = map(int,input().split())
a = list(map(int,input().split()))

route = []
multi = []

for i in range(2,len(a)+1):
    for j in itertools.combinations(a,i):
        if a[0] and a[len(a)-1] in j and abs(j[len(j)-1] - j[len(j)-2]) <= k:
            route.append(j)

for i in route:
    mul = 1
    for j in i:
        mul *= j

    multi.append(mul)

print(min(multi))
