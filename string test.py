a = list(map(int,input().split()))

middle = len(a)//2

be_middle = a[0:middle]
af_middle = a[middle+1:]

sub_a = [i for i in range(middle,0,-1)][::-1]

print(be_middle)
print(af_middle)
print(sub_a)
