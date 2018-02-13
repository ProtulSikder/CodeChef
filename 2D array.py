rows = int(input())
a = []

for i in range(rows):
    b = [int(j) for j in input().split()]
    a.append(b)

print(a)
