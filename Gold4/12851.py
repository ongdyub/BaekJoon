from collections import deque

N, K = map(int, input().split(' '))
visit = [False] * 100001
visit_cnt = [0] * 100001
visit_time = [0] * 100001

Q = deque()
Q.append((N,0))
visit_cnt[N] = 1
check = -1
cnt = 0

while len(Q) > 0:
    cur, step = Q.popleft()
    # print(f'{cur} {visit_cnt[cur]} {step}')
    visit[cur] = True
    
    if cur == K:
        # visit[cur] = False
        # check = step
        # cnt += 1
        break

    # if step == check+1 and check != -1:
    #     break

    if cur+1 < 100001:
        # 이미 방문상태인데 다른곳에서 온 경우 ex) 1->2 + and * +++ 같은 시간으로 와야 최소임
        if visit[cur+1]:
            if visit_time[cur+1] == step + 1:
                visit_cnt[cur+1] += visit_cnt[cur]
        else:
            # 첫 방문
            visit[cur+1] = True
            visit_cnt[cur+1] = visit_cnt[cur]
            visit_time[cur+1] = step + 1
            Q.append((cur+1, step+1))
    
    if cur-1 >= 0:
        if visit[cur-1]:
            if visit_time[cur-1] == step + 1:
                visit_cnt[cur-1] += visit_cnt[cur]
        else:
            # 첫 방문
            visit[cur-1] = True
            visit_cnt[cur-1] = visit_cnt[cur]
            visit_time[cur-1] = step + 1
            Q.append((cur-1, step+1))

    if cur*2 < 100001:
        if visit[cur*2]:
            if visit_time[cur*2] == step + 1:
                visit_cnt[cur*2] += visit_cnt[cur]
        else:
            # 첫 방문
            visit[cur*2] = True
            visit_cnt[cur*2] = visit_cnt[cur]
            visit_time[cur*2] = step + 1
            Q.append((cur*2, step+1))


print(step)
print(visit_cnt[K])