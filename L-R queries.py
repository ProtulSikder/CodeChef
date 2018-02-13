t = int(input())

for i in range(t):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    
    for z in range(q):
        typ,l,r = map(int,input().split())

        if typ == 1:
            maxi=[]

            for j in a:
                maxi.append((j-a[l-1])*(a[r-1]-j))

            print(max(maxi))

        elif typ == 2:
            a[l-1] = r
