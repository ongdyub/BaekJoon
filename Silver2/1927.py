import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
H = []

for _ in range(N):
    num = int(input())
    
    if num == 0:
        if len(H) == 0:
            print(0)
        else:
            print(heappop(H))
    else:
        heappush(H, num)
