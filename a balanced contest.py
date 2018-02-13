cases = int(input())

result = []

for i in range(cases):
    n, p = map(int,input().split())

    solve_num = list(map(int,input().split()))
    
    cake_count = 0
    hard_count = 0
    
    for j in range(n):
        if solve_num[j] >= p//2:
            cake_count += 1

        elif solve_num[j] <= p//10:
            hard_count += 1

    if cake_count == 1 and hard_count == 2:
        result.append('yes')

    else:
        result.append('no')

for i in result:
    print(i)
