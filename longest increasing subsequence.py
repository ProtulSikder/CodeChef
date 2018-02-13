seq = list(map(int,input().split(',')))

emp = [9999999999]

for i in range(len(seq)):
    for j in range(len(emp)):
        if seq[i] > emp[j]:
            emp.append(seq[i])

        else:
            while j < len(emp):
                del seq[j]
                j += 1

print(emp)
