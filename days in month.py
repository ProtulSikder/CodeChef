for _ in range(int(input())):
    d,w = input().split()
    week = ['mon','tues','wed','thurs','fri','sat','sun']
    mon,tues,wed,thurs,fri,sat,sun = 0,0,0,0,0,0,0

    a = week.index(w)

    for i in range(int(d)):
        if a == 0:
            mon += 1
        elif a == 1:
            tues += 1
        elif a == 2:
            wed += 1
        elif a == 3:
            thurs += 1
        elif a == 4:
            fri += 1
        elif a == 5:
            sat += 1
        elif a == 6:
            sun += 1
        a += 1
        a %= 7

    print('{} {} {} {} {} {} {}'.format(mon,tues,wed,thurs,fri,sat,sun))
