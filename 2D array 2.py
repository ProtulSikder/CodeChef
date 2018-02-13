n = int(input())

a = [[0]*n]*n

for i in range(n):
    for j in range(n):
        a[i][j] = int(input())
        print('value of a[{}][{}]:{}'.format(i,j,a[i][j]))

for i in range(n):
    for j in range(n):
        print(a[i][j])
