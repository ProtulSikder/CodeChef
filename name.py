t = int(input())
for i in range(t):
    naam = input().split()
    if len(naam) == 1:
        print(naam[0].capitalize())
    else:
        blah = ""
        for j in range(len(naam)-1):
            a = naam[j]
            blah = blah + a[0].upper() + '.' + ' '
        print(blah+naam[-1].capitalize())
