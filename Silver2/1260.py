from collections import deque

N, M, V = map(int, input().split(' '))

visit = [0] * (N+1)
graph = [[0]*(N+1) for i in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split(' '))
    graph[s][e] = 1
    graph[e][s] = 1
    
# DFS

Q = deque([V])
out = ''

while len(Q) > 0:
    cur = Q.popleft()
    if not visit[cur]:
        out += f'{cur} '
    visit[cur] = 1
    
    for e in range(N,0,-1):
        if graph[cur][e] == 1 and not visit[e]:
            Q.appendleft(e)
            
            
print(out)

# BFS
visit = [0] * (N+1)
Q = deque([V])
out = ''

while len(Q) > 0:
    cur = Q.popleft()
    if not visit[cur]:
        out += f'{cur} '
    visit[cur] = 1
    
    for e in range(1, N+1):
        if graph[cur][e] == 1 and not visit[e]:
            Q.append(e)
            
print(out)