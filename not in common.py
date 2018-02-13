t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    list_a = list(map(int,input().split()))
    list_b = list(map(int,input().split()))
    num = 0
    for j in list_a:
        if j in list_b:
            num += 1
    print(num)
    
