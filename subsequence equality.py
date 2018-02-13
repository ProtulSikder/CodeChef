t = int(input())

result = []

for i in range(t):
    string = input()
    
    for j in string:
       occurance = string.count(j)

       if occurance >= 2:
           result.append('yes')
           break

    else:
        result.append('no')

for i in result:
    print(i)
