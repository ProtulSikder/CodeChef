a=[1,2,3,4,5]

for m in range(len(a)-1):
    for n in range(m+1,len(a)):
        print(a[m]*a[n])
