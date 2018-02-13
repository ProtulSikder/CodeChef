t = int(input())
for i in range(t):
    a = input()
    balance = 0
    max_balance = 0
    s = ''
    for j in a:
        if j == '(':
            balance += 1
        else:
            balance -= 1
        max_balance = max(max_balance,balance)
    for j in range(max_balance):
        s += '('
    for j in range(max_balance):
        s += ')'
    print(s)
