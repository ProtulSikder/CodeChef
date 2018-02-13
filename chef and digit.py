for i in range(int(input())):
    s = input()
    one = s.count('1')
    zero = s.count('0')
    if one == 1 or zero == 1:
        print('Yes')
    else:
        print('No')
