from collections import deque

N, M = map(int, input().split(' '))

visit = [[False]*M for i in range(N)]

graph = [['']*M for i in range(N)]

Q = deque()
cnt = 0

for _ in range(N):
    cmd = input()
    for idx in range(M):
        graph[_][idx] = cmd[idx]
        
        # if cmd[idx] == 'I':
        #     Q.append((_, idx))

Q.append((0,0,1))

while len(Q) > 0:
    cur_x, cur_y, step = Q.popleft()
    
    if cur_x == N-1 and cur_y == M-1:
        step += 1
        break
    # print(cur_x, cur_y)
    if visit[cur_x][cur_y] or graph[cur_x][cur_y] == '0':
        visit[cur_x][cur_y] = True
        continue
    else:
        visit[cur_x][cur_y] = True
        
        ad_x = cur_x+1 if cur_x < N-1 else N-1
        mi_x = cur_x-1 if cur_x > 0 else 0
        ad_y = cur_y+1 if cur_y < M-1 else M-1
        mi_y = cur_y-1 if cur_y > 0 else 0
        # print(f'{cur_x} {cur_y} {cur_x} {ad_y} {step}')
        if not visit[cur_x][ad_y]:
            Q.append((cur_x, ad_y, step+1))
        if not visit[cur_x][mi_y]:
            Q.append((cur_x, mi_y, step+1))
        if not visit[ad_x][cur_y]:
            Q.append((ad_x, cur_y, step+1))
        if not visit[mi_x][cur_y]:
            Q.append((mi_x, cur_y, step+1))

print(step-1)