t = int(input())
for i in range(t):
    my_li = list(map(int,input().split()))
    my_li.remove(len(my_li)-1)
    print(max(my_li))
    
