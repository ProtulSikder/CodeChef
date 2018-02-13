n,k = map(int,input().split())
nums = 0
for i in range(n):
    num = int(input())
    if num % k == 0:
        nums += 1
print(nums)
