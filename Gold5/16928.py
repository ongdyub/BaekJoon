from collections import deque

N, M = map(int, input().split(' '))
check = 0

visit = [False]*101

graph = [0]*101
Q = deque()

for _ in range(N+M):
    s, e = map(int, input().split(' '))
    graph[s] = e
        
Q.append((1, 0))

while len(Q) > 0:
    (cur, step) = Q.popleft()
    # print("start")
    # print(f'{cur} {step}')
    if cur == 100:
        break

    if visit[cur]:
        continue
    else:
        visit[cur] = True
        
        if cur+1 < 101 and not visit[cur+1] and cur+1 < 101:
            if graph[cur+1]:
                Q.append((graph[cur+1], step+1))
            else:
                Q.append((cur+1, step+1))
                
        if cur+2 < 101 and not visit[cur+2] and cur+2 < 101:
            if graph[cur+2]:
                Q.append((graph[cur+2], step+1))
            else:
                Q.append((cur+2, step+1))
                
        if cur+3 < 101 and not visit[cur+3] and cur+3 < 101:
            if graph[cur+3]:
                Q.append((graph[cur+3], step+1))
            else:
                Q.append((cur+3, step+1))
                
        if cur+4 < 101 and not visit[cur+4] and cur+4 < 101:
            if graph[cur+4]:
                Q.append((graph[cur+4], step+1))
            else:
                Q.append((cur+4, step+1))
                
        if cur+5 < 101 and not visit[cur+5] and cur+5 < 101:
            if graph[cur+5]:
                Q.append((graph[cur+5], step+1))
            else:
                Q.append((cur+5, step+1))
                
        if cur+6 < 101 and not visit[cur+6] and cur+6 < 101:
            if graph[cur+6]:
                Q.append((graph[cur+6], step+1))
            else:
                Q.append((cur+6, step+1))
        
print(step)