import heapq

N = int(input())

n_Q = []
p_Q = []

for _ in range(N):
    cmd = int(input())
    
    if not cmd:
        if len(n_Q) == 0 and len(p_Q) == 0:
            print(0)
            continue
        else:
            if len(n_Q) == 0:
                print(heapq.heappop(p_Q))
            elif len(p_Q) == 0:
                print(-heapq.heappop(n_Q))
            else:
                n = n_Q[0]
                p = p_Q[0]
                if p < n:
                    print(p)
                    heapq.heappop(p_Q)
                else:
                    print(-n)
                    heapq.heappop(n_Q)
    else:
        if cmd > 0:
            heapq.heappush(p_Q, cmd)
        else:
            heapq.heappush(n_Q, -cmd)