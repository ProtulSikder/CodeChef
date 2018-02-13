t = int(input())

for i in range(t):
    n = int(input())

    a = list(map(int,input().split()))

    if 0 not in a:
        print(0)

    else:
        for j in range(len(a)):
            if a[j] == 0:
                new_list = a[j:]
                print(len(new_list)*1100 - new_list.count(1)*1000)
                break

    
