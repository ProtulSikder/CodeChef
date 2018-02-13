n = input()
s = list(map(int,input().split()))

odd = 0
even = 0

for i in s:
    if i%2 == 0:
        even += 1
    else:
        odd += 1

print('READY FOR BATTLE' if even > odd else 'NOT READY')
