from collections import deque

n, m = map(int, input().split(' '))

visit = [[False]*m for i in range(n)]
graph = [[0]*m for i in range(n)]
output = [['-1']*m for i in range(n)]

start_x = 0
start_y = 0

for _ in range(n):
    l = list(map(int, input().split(' ')))
    if 2 in l:
        start_x = _
        start_y = l.index(2)
    graph[_] = l

# 2 위치 찾기

Q = deque([(start_x, start_y, 0)])
step = 0

while len(Q) > 0:
    (cur_x, cur_y, step) = Q.popleft()
    
    if visit[cur_x][cur_y]:
        continue
    else:
        visit[cur_x][cur_y] = True
        
        if graph[cur_x][cur_y] == 0:
            output[cur_x][cur_y] = str('0')
            continue
        else:
            output[cur_x][cur_y] = str(step)
        
        ad_x = cur_x+1 if cur_x < n-1 else n-1
        mi_x = cur_x-1 if cur_x > 0 else 0
        ad_y = cur_y+1 if cur_y < m-1 else m-1
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
        
for x in range(n):
    for y in range(m):
        if output[x][y] == '-1' and graph[x][y] == 0 and not visit[x][y]:
            output[x][y] = '0'

for _ in range(n):
    # print(output[_])
    print(' '.join(output[_]))