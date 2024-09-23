import sys

def check_pattern(num):
    return int(num ** 0.5) ** 2 == num

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

max_square = -1

for dx in range(-n, n):
    for dy in range(-m, m):
        if dx == 0 and dy == 0:
            continue

        for i in range(n):
            for j in range(m):
                x, y = i, j
                num = 0

                while 0 <= x < n and 0 <= y < m:
                    num = num * 10 + board[x][y]

                    if check_pattern(num):
                        max_square = max(max_square, num)

                    x += dx
                    y += dy

# 결과 출력
print(max_square)
