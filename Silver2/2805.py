N, M = map(int, input().split(' '))

woods = list(map(int, input().split(' ')))

short = 0
high = max(woods)

while short < high:
    cnt = 0
    mid = (short+high)//2
    # print(mid)
    for w in woods:
        if w-mid > 0:
           cnt += w-mid
    # print(cnt)
    # 높이 내려야함
    if cnt < M:
        high = mid
    else:
        short = mid+1
        
print(short-1)