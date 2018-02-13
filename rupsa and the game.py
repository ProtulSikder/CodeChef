mod = 10**9 + 7

def rgame(a, n):
    s = 2 * a[0]
    ans = 0
    p = 1
    for i in range(1, n + 1):
        p = (2 * p) % mod
        ans = (2 * ans + s * a[i]) % mod
        s = (s + p * a[i]) % mod
    return ans

t = int(input())
answers = []

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    answers.append(rgame(a, n))

for i in answers:
    print(i)
