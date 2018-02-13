my_list = []
while 1:
    a = input()
    if a:
        my_list.append(a)
    else:
        break
for i in my_list:
    chef = []
    oppo = []
    for j in range(len(i)):
        if j%2 == 0:
            chef.append(i[j])
        else:
            oppo.append(i[j])
    print(chef)
    print(oppo)
