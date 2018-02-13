import string
t = int(input())

alpha = list(string.ascii_lowercase)

text = ['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth','Ninth','Tenth']

for i in range(t):
    n = list(map(int,input().split()))

    s = input()

    miss_letter = []
    let_cost = []

    for j in range(len(alpha)):
        if alpha[j] not in s:
            miss_letter.append(alpha[j])
            let_cost.append(n[j])

    

    print(text[0] + " test")

    if len(miss_letter) != 0:
        print("There are {} letters missing from the original string: ".format(text[len(miss_letter)].lower()),end="")
        

    
