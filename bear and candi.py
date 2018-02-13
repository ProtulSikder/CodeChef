t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    turn = 1
    lim = 0
    bob = 0
    while 1:
        if turn % 2 == 1:
            lim += turn
            if lim > a:
                print('Bob')
                break
        else:
            bob += turn
            if bob > b:
                print('Limak')
                break
        turn += 1
