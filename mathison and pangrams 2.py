import string
t = int(input())

alpha = list(string.ascii_lowercase)

for i in range(t):
    n = list(map(int,input().split()))

    s = input()

    sum = 0

    for j in range(26):
        if alpha[j] not in s:
            sum += n[j]

    print(sum)
