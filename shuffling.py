t = int(input())

for i in range(t):
    m,x,y = map(int,input().split())

    a = [j for j in range(1,m+1)]

    while len(a) > 2:
        even_a,odd_a = [],[]

        for j in range(len(a)):
            if j%2 == 0:
                even_a.append(a[j])

            else:
                odd_a.append(a[j])

        remv = len(even_a)*x//y

        even_a.pop(remv)
        odd_a.pop(remv)

        a = even_a + odd_a

    print(a[0]^a[1])
