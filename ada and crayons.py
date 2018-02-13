t = int(input())
for i in range(t):
    n = input()
    flag = 0
    string = '0'
    temp = n[0]
    for i in n:
        if i != temp:
            temp = i
            if flag%2 == 0:
                string += '1'
            else:
                string += '0'
            flag += 1
    num_0 = string.count('0')
    num_1 = string.count('1')
    if num_0 < num_1:
        print(num_0)
    else:
        print(num_1)
