known = input()
n = int(input())
for i in range(n):
    test = input()
    for j in test:
        if j not in known:
            print('No')
            break
    else:
        print('Yes')
