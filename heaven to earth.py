import math
t = int(input())
for i in range(t):
    n,vs,ve = map(int,input().split())
    print('Elevator' if (2*n)/ve < (math.sqrt(2)*n/vs) else 'Stairs')
