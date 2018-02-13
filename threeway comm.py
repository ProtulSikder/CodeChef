def my_func(dx,dy,r):
    return dx**2 + dy**2 <= r*r

for _ in range(int(input())):
    d = int(input())
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())

    pair = 0

    if my_func((x1-x2),(y1-y2),d):
        pair += 1
    if my_func((x1-x3),(y1-y3),d):
        pair += 1
    if my_func((x2-x3),(y2-y3),d):
        pair += 1

    print('yes' if pair >1 else 'no')
