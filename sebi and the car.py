t = int(input())

rest = []

for i in range(t):
    s,sg,fg,d,t = map(int,input().split())

    real_speed = s + (180*d)/t

    abs_s = abs(real_speed - sg)
    abs_f = abs(real_speed - fg)

    if abs_s != abs_f:
        mini = min(abs_s,abs_f)

        if mini == abs_s:
            rest.append('SEBI')
            print(mini)

        else:
            rest.append('FATHER')
            print(mini)

    else:
        rest.append('DRAW')

for i in rest:
    print(i)
