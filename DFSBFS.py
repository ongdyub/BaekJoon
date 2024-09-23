from collections import deque

M, N = map(int, input().split(' '))
check = 0

visit = [[False]*M for i in range(N)]
visit_cnt = 0

graph = [[0]*M for i in range(N)]
Q = deque()

for x in range(N):
    l = list(map(int, input().split(' ')))
    for y in range(M):
        if l[y] == 1:
            Q.append((x, y, 0))
        if l[y] != -1:
            check += 1
        graph[x][y] = l[y]
        
while len(Q) > 0:
    (cur_x, cur_y, step) = Q.popleft()

    if visit[cur_x][cur_y]:
        continue
    else:
        visit[cur_x][cur_y] = True
        
        if graph[cur_x][cur_y] == -1:
            continue
        # else:
        #     output[cur_x][cur_y] = str(step)
        visit_cnt += 1
        
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

    if visit_cnt == check:
        break
# print(len(visit_Q))
# print(visit_cnt)
# print(check)

if visit_cnt == check:
    print(step)
else:
    print(-1)