t = int(input())

for i in range(t):
    n = int(input())

    b = []
    a = []
    
    for j in range(n):
        encode = int(input())

        num_b = encode>>16
        
        unenc = num_b << 16

        num_a = encode - unenc

        b.append(num_b)
        a.append(num_a)

    print("Case {}:".format(i+1))
    print(*a)
    print(*b)
