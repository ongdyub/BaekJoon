from collections import deque

N, K = map(int, input().split(' '))
visit = [False] * 100001
cnt_visit = [0] * 100001

Q = deque()
Q.append((N,0))
check = -1
cnt = 0

while len(Q) > 0:
    cur, step = Q.popleft()
    print(f'{cur} {step}')
    visit[cur] = True
    
    if step == check+1 and check != -1:
        break
    
    if cur == K:
        visit[cur] = False
        check = step
        cnt += 1
        continue

    if cur+1 < 100001 and not visit[cur+1]:
        if cur+1 == K:
            visit[cur+1] = False
        else:
            visit[cur+1] = True
        Q.append((cur+1, step+1))
        
    if cur-1 >= 0 and not visit[cur-1]:
        if cur-1 == K:
            visit[cur-1] = False
        else:
            visit[cur-1] = True
        Q.append((cur-1, step+1))
        
    if cur*2 < 100001 and not visit[cur*2]:
        if cur*2 == K:
            visit[cur*2] = False
        else:
            visit[cur*2] = True
        Q.append((cur*2, step+1))


print(check)
print(cnt)