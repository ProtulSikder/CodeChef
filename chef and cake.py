t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    summ = 0
    for j in range(n):
        string = list(input())
        for k in range(len(string)-1):
            if string[k] == string[k+1]:
                if string[k+1] == 'R':
                    string[k+1] = 'G'
                    summ += 5
                else:
                    string[k+1] = 'R'
                    summ += 3
    print(summ)
            
