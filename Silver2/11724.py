from collections import deque

N, M = map(int, input().split(' '))

visit = [False for i in range(N+1)]
graph = [[0]*(N+1) for i in range(N+1)]

# print(visit)

for _ in range(M):
    s, e = map(int, input().split(' '))
    graph[s][e] = 1
    graph[e][s] = 1
    
connect = 0

for i in range(1, N+1):
    if visit[i]:
        continue
    else:
        Q = deque([i])
        
        while len(Q) > 0:
            cur = Q.popleft()
            for e in range(1, N+1):
                if graph[cur][e] == 1 and not visit[e]:
                    visit[e] = True
                    Q.appendleft(e)
        connect += 1
        
print(connect)
                    