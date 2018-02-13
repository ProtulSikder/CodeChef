import re

for _ in range(int(input())):
    s = input()

    a = re.findall(r'<>',s)

    print(len(a))
