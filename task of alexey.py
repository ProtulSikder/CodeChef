import psyco

psyco.full()

t = int(input())

result = []

def find_lcm(a,b):
    max_num = max(a,b)
    
    while 1:
        if a > b:
            m = a
            n = b
        else:
            n = a
            m = b
        i = 1
        while 1:
            if m % n == 0:
                return m
            i += 1
            m = max(a,b) * i

for i in range(t):
    n = int(input())
    
    lcm = []
    
    sensors = list(map(int,input().split()))

    for j in range(len(sensors)-1):
        for k in range(j+1,len(sensors)):
            lcm.append(find_lcm(sensors[j],sensors[k]))

    result.append(min(lcm))

for i in result:
    print(i)
