t = int(input())
for i in range(t):
    n = int(input())
    j = 1
    zeros = 0
    while 1:
        if n // 5**j > 0:
            zeros += n//5**j
            j += 1
        else:
            break
    print(zeros)
    
