from collections import deque

N = int(input())

graph = [[0]*N for i in range(N)]
output = [['0']*N for i in range(N)]

for x in range(N):
    cmd = list(map(int, input().split(' ')))
    for y in range(N):
        graph[x][y] = cmd[y]
        
for start in range(N):
    Q = deque([start])
    visit = [False]*N
    
    while len(Q) > 0:
        cur = Q.popleft()
        
        if visit[cur]:
            continue
        else:
            visit[cur] = True
            for i in range(N):
                if visit[i] and graph[cur][i] and i == start:
                    output[start][start] = '1'
                if not visit[i] and graph[cur][i]:
                    Q.append(i)
                    output[start][i] = '1'
                    
for o in output:
    print(' '.join(o))
        
    