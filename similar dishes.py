t = int(input())
for i in range(t):
    d_one = input().split()
    d_two = input().split()
    num = 0
    for j in d_one:
        if j in d_two:
            num += 1
        if num == 2:
            print('similar')
            break
    else:
        print('dissimilar')
