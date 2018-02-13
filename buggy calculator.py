cases = int(input())

total = []

for i in range(cases):
    num1,num2 = input().split(' ')

    result = ''

    if len(num1) != len(num2):
        mini_num = min(int(num1),int(num2))
        max_num = max(int(num1),int(num2))

        mini_str = str(mini_num)
        max_str = str(max_num)

        diff = len(max_str) - len(mini_str)

        if mini_num == int(num1):
            num1 = diff*'0' + num1

        else:
            num2 = diff*'0' + num2

    for m in range(len(num1)):
        sum = int(num1[m]) + int(num2[m])

        remain = sum%10

        result += str(remain)

    total.append(int(result))

for i in total:
    print(i)
