cases = int(input())

median = []

for i in range(cases):
    n,k = map(int,input().split())

    index = (n+k)//2

    the_list = list(map(int,input().split()))

    the_list.sort()

    median.append(the_list[index])

for i in median:
    print(i)
