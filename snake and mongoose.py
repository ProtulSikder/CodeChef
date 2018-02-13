t = int(input())

for i in range(t):
    s = input()
    s = [a for a in s]
    j = 0

    while j < len(s)-1:
        if s[j] == 's' and s[j+1] == 'm':
            s[j] = 'e'
            j += 2

        elif s[j] == 'm' and s[j+1] == 's':
            s[j+1] = 'e'
            j += 2

        else:
            j += 1

    sn = s.count('s')
    mn = s.count('m')

    if sn == mn:
        print('tie')

    elif sn > mn:
        print('snakes')

    else:
        print('mongooses')
