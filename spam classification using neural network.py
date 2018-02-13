for _ in range(int(input())):
    n,min_x,max_x = map(int,input().split())
    
    nets = []
    
    for i in range(n):
        a = list(map(int,input().split()))
        nets.append(a)

    spam = 0
    not_spam = 0

    for i in range(min_x,max_x+1):
        temp = i
        for j in range(len(nets)):
            x = (nets[j][0]*temp) + nets[j][1]
            temp = x
        if temp % 2 == 0:
            not_spam += 1
        else:
            spam += 1

    print(str(not_spam) + ' ' + str(spam))
            
