n = int(input(""))
a = input("")
a = a.split(' ')
b = list(range(1,n+1))
for i in a:
    if int(i) in b:
        b.remove(int(i))
print(' '.join(map(str,b)))
