import math

n = int(input())
m = int(input())

graph = dict()
dist = [[math.inf]*(n+1) for _ in range(n+1)]

for _ in range(n+1):
    graph[_] = dict()
    graph[_][_] = 0
    dist[_][_] = 0

for _ in range(m):
    s, e, w = map(int, input().split(' '))
    
    if e in graph[s] and w > graph[s][e]:
        continue
    
    graph[s][e] = w
    dist[s][e] = w
    
# print(graph)
# print(dist)


for k in range(0,n+1):
    for i in range(0,n+1):
        for j in range(0,n+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
            
for _ in range(1,n+1):
    ans = ''
    for __ in range(1, n+1):
        if dist[_][__] == math.inf:
            ans += '0 '
        else:
            ans += f'{dist[_][__]} '
    print(ans[:-1])