t = int(input())
for i in range(t):
    n,k,e,m = map(int,input().split())
    marks = []
    for j in range(n-1):
        mark = list(map(int,input().split()))
        marks.append(sum(mark))
    sg = list(map(int,input().split()))
    marks.sort(reverse=True)
    if marks[k-1] > sum(sg)+m:
        print('Impossible')
    else:
        print(max(marks[k-1]-sum(sg)+1,0))
