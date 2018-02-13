w,b = map(float,input().split())
if w+.50 <= b and w%5 == 0:
    print('%.2f'%(b-w-.50))
else:
    print('%.2f'%b)
