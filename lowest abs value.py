a = list(map(int,input().split()))
a.sort()
summ = abs(a[0]-a[1]) + abs(a[-1]-a[-2])
for i in range(2,len(a)-2):
    if abs(a[i-1]-a[i]) <= abs(a[i]-a[i+1]):
        summ += abs(a[i-1]-a[i])
    else:
        summ += abs(a[i]-a[i+1])
print(summ)
