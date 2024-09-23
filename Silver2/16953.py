from collections import deque

A, B = map(int, input().split(' '))

Q = deque()
Q.append((A,0))
visit = set()

ans = -2

while len(Q) > 0:
    cur, step = Q.popleft()
    
    if cur == B:
        ans = step
        break
    
    visit.add(cur)
    
    add = int(str(cur)+'1')
    mul = cur * 2
    
    if not add in visit and add <= B:
        Q.append((add, step+1))
        
    if not mul in visit and mul <= B:
        Q.append((mul, step+1))

print(ans+1)