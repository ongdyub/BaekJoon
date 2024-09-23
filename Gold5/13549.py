from collections import deque

N, K = map(int, input().split(' '))
visit = [False] * 100001

Q = deque()
Q.append((N,0))

while len(Q) > 0:
    cur, step = Q.popleft()
    # print(f'{cur} {step}')
    visit[cur] = True
    teleport = cur
    in_teleport = False
    
    if cur == K:
        break
    
    if cur < K and cur != 0:
        while teleport <= K:
            teleport *= 2
            
            if teleport == K:
                in_teleport = True
                break
            
            if teleport < 100001 and not visit[teleport]:
                visit[teleport] = True
                Q.appendleft((teleport, step))
    
    if in_teleport:
        break
    
    if cur+1 < 100001 and not visit[cur+1]:
        visit[cur+1] = True
        Q.append((cur+1, step+1))
        
    if cur-1 >= 0 and not visit[cur-1]:
        visit[cur-1] = True
        Q.append((cur-1, step+1))


print(step)