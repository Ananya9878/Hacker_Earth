for _ in range(int(input())):
    n = int(input())
    s = input()
    t = input()
    d1={'?':0}
    d2={'?':0}
    for i in range(n):
        if s[i] not in d1:
            d1[s[i]] = 1
        else:
            d1[s[i]]+=1

    for i in range(n):
        if t[i] not in d2:
            d2[t[i]] = 1
        else:
            d2[t[i]]+=1

    for i in d1:
        if i in d2 and i != '?':
            m = min(d1[i],d2[i])
            d1[i]-=m
            d2[i]-=m

    s1,s2 = 0,0
    for i in d1:
        if i != '?':
            s1+=d1[i]

    for i in d2:
        if i != '?':
            s2+=d2[i]

    if s1 == 0 and s2 == 0 and d1['?'] == d2['?']:
        print('YES')
    elif s1 == d2['?'] and s2 == d1['?']:
        print('YES')
    else:
        print('NO')







