t = int(input())

for i in range(t):
    num,nation = input().split()
    laddu = 0
    for j in range(int(num)):
        my_list = list(input().split())

        if my_list[0] == 'CONTEST_WON':
            if int(my_list[1]) <= 20:
                laddu += 300 + 20 - int(my_list[1])
            else:
                laddu += 300

        elif my_list[0] == 'TOP_CONTRIBUTOR':
            laddu += 300

        elif my_list[0] == 'BUG_FOUND':
            laddu += int(my_list[1])

        elif my_list[0] == 'CONTEST_HOSTED':
            laddu += 50
    
    if nation == 'INDIAN':
        print(laddu//200)
    else:
        print(laddu//400)
