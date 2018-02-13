n,k = map(int,input().split())

a = [1] * n

def sum(a,n,k):
    sum  = 0

    for i in range(k,n):
        sum += a[i]

    return sum

for i in range(n):
    if i+1 <= k :
        a[1] = 1

    else:
        a[i] = sum(a,i,i-k)

print(a[i]%1000000007)
