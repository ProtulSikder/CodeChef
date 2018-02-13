from fractions import Fraction as f 
t = int(input())

def solve():
    s,sg,fg,d,t = map(int,input().split())

    actual = s + f(d*50*60*60,t*1000)

    asg = abs(sg - actual)
    afg = abs(fg - actual)

    return 'SEBI' if asg < afg else 'FATHER' if asg > afg else 'DRAW'

for i in range(t):
    print(solve())
