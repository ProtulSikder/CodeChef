problems = ['cakewalk','simple','easy','easy-medium','medium','medium-hard','hard']
rslt = []

t = int(input())

for i in range(t):
    prb_no = [0,0,0,0,0,0,0]
    n = int(input())

    for j in range(n):
        while 1:
            string = input()

            if string in problems:
                ind = problems.index(string)
                prb_no[ind] += 1
                break

    if prb_no[0] and prb_no[1] and prb_no[2] and (prb_no[3] or prb_no[4]) and (prb_no[5] or prb_no[6]):
        rslt.append('Yes')

    else:
        rslt.append('No')

for i in rslt:
    print(i)

        
