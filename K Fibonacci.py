def sum(a,n,k):
    sum=0
    for i in range(k,n):
        sum+=a[i]
        print(sum)
        
    return sum
 
n,k=map(int,input().split())

a=[1]*n

for i in range(n):
    if i+1<=k:
        a[i] = 1
    else:
        a[i] = sum(a,i,i-k)
print(a)
