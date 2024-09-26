from collections import deque

N, M = map(int, input().split(' '))

graph = []
visit = [[False]*M for _ in range(N)]
check = [[-1]*M for _ in range(N)]
for _ in range(N):
    row = input()
    row_data = []
    for r in row:
        row_data.append(int(r))
    graph.append(row_data)
    
Q = deque()
# x y step break
Q.append((0,0,1,False))
visit[0][0] = True
goal = False

while len(Q) > 0:
    x, y, step, brk = Q.popleft()
    # print(f'{x} {y} {step} {brk}')
    if x == N-1 and y == M-1:
        goal = True
        break
    
    xup = max(0, x-1)
    xdown = min(N-1, x+1)
    yright = min(M-1, y+1)
    yleft = max(0, y-1)
    
    if not visit[xup][y]:
        if graph[xup][y]:
            if brk:
                pass
            else:
                visit[xup][y] = True
                Q.append((xup, y, step+1, True))
        else:
            visit[xup][y] = True
            Q.append((xup, y, step+1, brk))
            
    if not visit[xdown][y]:
        if graph[xdown][y]:
            if brk:
                pass
            else:
                visit[xdown][y] = True
                Q.append((xdown, y, step+1, True))
        else:
            visit[xdown][y] = True
            Q.append((xdown, y, step+1, brk))
            
    if not visit[x][yleft]:
        if graph[x][yleft]:
            if brk:
                pass
            else:
                visit[x][yleft] = True
                Q.append((x, yleft, step+1, True))
        else:
            visit[x][yleft] = True
            Q.append((x, yleft, step+1, brk))
            
    if not visit[x][yright]:
        if graph[x][yright]:
            if brk:
                pass
            else:
                visit[x][yright] = True
                Q.append((x, yright, step+1, True))
        else:
            visit[x][yright] = True
            Q.append((x, yright, step+1, brk))
            
if goal:
    print(step)
else:
    print(-1)