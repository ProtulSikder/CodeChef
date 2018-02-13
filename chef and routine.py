t = int(input())

for i in range(t):
    s = input()

    dcit = {'C':0,'E':1,'S':2}

    for j in range(len(s)-1):
        if dcit[s[j]] > dcit[s[j+1]]:
            print('no')
            break

    else:
        print('yes')
