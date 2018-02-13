t = int(input())
for i in range(t):
    a = input()
    b = input()
    for j in a:
        if j in b:
            print('Yes')
            break
    else:
        print('No')
