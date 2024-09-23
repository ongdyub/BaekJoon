N = int(input())

square = [[0]*N for i in range(N)]
detect = [[False]*N for i in range(N)]

for _ in range(N):
    line = list(map(int, input().split(' ')))
    square[_] = line
    
blue = 0
white = 0
recur = 1

# print(square[2:5])
# print(sum(square[2]))
# print(sum(square[4]))
while N > 0:
    for x in range(recur):
        for y in range(recur):
            if detect[x*N][y*N]:
                # print("DEE")
                continue
            else:
                value = 0
                candidate = square[x*N : (x+1)*N]
                for can in candidate:
                    value += sum(can[y*N : (y+1)*N])
                # print(value)

                if value == N**2:
                    candidate = detect[x*N : (x+1)*N]
                    for can in candidate:
                        can[y*N : (y+1)*N] = [True] * N
                    blue += 1
                elif value == 0:
                    candidate = detect[x*N : (x+1)*N]
                    for can in candidate:
                        can[y*N : (y+1)*N] = [True] * N
                    white += 1
                else:
                    continue
    N //= 2
    recur *= 2
    
print(white)
print(blue)