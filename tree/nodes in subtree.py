def addd(d1,d2):
    for i in d2:
        if i in d1:
            d1[i]+=d2[i]
        else:
            d1[i] = d2[i]
    return d1

def dfs(g,node,v,s,res):
    if node in v:
        return {}
    else:
        v.add(node)
    d = {}
    for i in g[node]:
        k=dfs(g,i,v,s,res)
        d = addd(d,k)
    c = s[node-1]
    if c in d:
        d[c]+=1
    else:
        d[c] = 1
    res[node] = d
    return d

def create(n):
    d = {}
    for i in range(n-1):
        u,v = map(int,input().split())
        if u not in d:
            d[u] = [v]
        else:
            d[u].append(v)
        if v not in d:
            d[v] = [u]
        else:
            d[v].append(u)
    return d

n,q = map(int,input().split())
s = input()
graph = create(n)
res = {}

dfs(graph,1,set(),s,res)
# print(res)
for i in range(q):
    u,c = input().split()
    x = res[int(u)]
    if c in x:
        print(x[c])
    else:
        print(0)

