for _ in range(int(input())):
    n,k = map(int,input().split())
    m_li = []
    for i in range(1,k+1):
        m_li.append(n%i)
    print(max(m_li))
