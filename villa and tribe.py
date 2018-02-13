t = int(input())
for i in range(t):
    s = input()
    a = s.count('A')
    b = s.count('B')
    for j in range(len(s)):
        if s[j] == 'A':
            start = j
            for k in range(j+1,len(s)):
                if s[k] == 'B':
                    start = 0
                    break
                elif s[k] == 'A':
                    end = k
                    temp = s[start:end+1]
                    a += temp.count('.')
                    break
        elif s[j] == 'B':
            start = j
            for k in range(j+1,len(s)):
                if s[k] == 'A':
                    start = 0
                    break
                elif s[k] == 'B':
                    end = k
                    temp = s[start:end+1]
                    b += temp.count('.')
                    break
    print('{} {}'.format(a,b))
                

        
