from collections import deque

T = int(input())

ans = []

for _ in range(T):
    A, B = map(int, input().split(' '))
    visit = [0] * 10001
    Q = deque()
    Q.append(('', 0, A))
    
    while len(Q) > 0:
        (operation, step, num) = Q.popleft()
        visit[num] = 1
        
        if num == B:
            break
        
        nxt = (num * 2) % 10000
        if not visit[nxt]:
            visit[nxt] = 1
            Q.append((operation+'D', step+1, nxt))
            
        nxt = num-1 if num > 0 else 9999
        if not visit[nxt]:
            visit[nxt] = 1
            Q.append((operation+'S', step+1, nxt))
        
        # 4
        if num // 1000 > 0:
            nxt = int(str(num)[1:]+str(num)[0])
            if not visit[nxt]:
                visit[nxt] = 1
                Q.append((operation+'L', step+1, nxt))
        else:
            nxt = num*10
            if not visit[nxt]:
                visit[nxt] = 1
                Q.append((operation+'L', step+1, nxt))
            
        if num // 1000 > 0:
            nxt = int(str(num)[-1]+str(num)[0:3])
            if not visit[nxt]:
                visit[nxt] = 1
                Q.append((operation+'R', step+1, nxt))
        else:
            nxt = num//10 + (num%10)*1000
            if not visit[nxt]:
                visit[nxt] = 1
                Q.append((operation+'R', step+1, nxt))
    
    ans.append(operation)

for a in ans:
    print(a)