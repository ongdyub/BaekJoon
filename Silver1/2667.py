from collections import deque

N = int(input())
no_cnt = 0

visit = [[False]*N for i in range(N)]
apart_cnt = []

graph = [[0]*N for i in range(N)]

for x in range(N):
    l = input()
    for y in range(N):
        graph[x][y] = int(l[y])
# print(graph)
for x in range(N):
    for y in range(N):
        if not visit[x][y] and graph[x][y]:
            Q = deque()
            Q.append((x, y))
            apart = 0
            # print("STart")
            while len(Q) > 0:
                (cur_x, cur_y) = Q.popleft()
                # print(f'{cur_x} {cur_y}')
                if visit[cur_x][cur_y]:
                    continue
                else:
                    visit[cur_x][cur_y] = True
                    apart += 1
                    ad_x = cur_x+1 if cur_x < N-1 else N-1
                    mi_x = cur_x-1 if cur_x > 0 else 0
                    ad_y = cur_y+1 if cur_y < N-1 else N-1
                    mi_y = cur_y-1 if cur_y > 0 else 0
                    # print(f'{cur_x} {cur_y} {cur_x} {ad_y} {step}')
                    if not visit[cur_x][ad_y] and graph[cur_x][ad_y]:
                        Q.append((cur_x, ad_y))
                    if not visit[cur_x][mi_y] and graph[cur_x][mi_y]:
                        Q.append((cur_x, mi_y))
                    if not visit[ad_x][cur_y] and graph[ad_x][cur_y]:
                        Q.append((ad_x, cur_y))
                    if not visit[mi_x][cur_y] and graph[mi_x][cur_y]:
                        Q.append((mi_x, cur_y))
            no_cnt += 1
            apart_cnt.append(apart)

        else:
            continue

# print(len(visit_Q))
# print(visit_cnt)
# print(check)

print(no_cnt)
apart_cnt.sort()
for a in apart_cnt:
    print(a)