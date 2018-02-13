t = int(input())

all_list = ['cakewalk','simple','easy','easy-medium','medium','medium-hard','hard']

valid_list_1 = ['cakewalk','simple','easy','easy-medium','hard']
valid_list_2 = ['cakewalk','simple','easy','medium','medium-hard']
valid_list_3 = ['cakewalk','simple','easy','easy-medium','medium-hard']
valid_list_4 = ['cakewalk','simple','easy','medium','hard']

result = []

for i in range(t):
    n = int(input())

    prb_list = []

    for j in range(n):
        while 1:
            string = input()

            if string in all_list:
                prb_list.append(string)
                break

    if set(valid_list_1).issubset(set(prb_list)) or set(valid_list_2).issubset(set(prb_list)) or set(valid_list_3).issubset(set(prb_list)) or set(valid_list_4).issubset(set(prb_list)):
        result.append('Yes')

    else:
        result.append('No')

for i in result:
    print(i)
