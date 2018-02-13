result = []

t = int(input())

for i in range(t):
    n = int(input())

    valid_dict = {'cakewalk':0,
              'simple':0,
              'easy':0,
              'easy-medium':0,
              'medium':0,
              'medium-hard':0,
              'hard':0}

    for j in range(n):
        while 1:
            string = input()

            if string in list(valid_dict.keys()):
                valid_dict[string] += 1
                break

    if valid_dict['cakewalk'] and valid_dict['simple'] and valid_dict['easy'] and (valid_dict['easy-medium'] or valid_dict['medium']) and (valid_dict['medium-hard'] or valid_dict['hard']):
        result.append('Yes')

    else:
        result.append('No')

for i in result:
    print(i)     
