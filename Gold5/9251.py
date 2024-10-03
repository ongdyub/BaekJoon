X = input()
Y = input()

i, j = len(X), len(Y)

dp = [[0]*(j+1) for _ in range(i+1)]

for x in range(1,i+1):
    for y in range(1,j+1):
        if X[x-1] == Y[y-1]:
            dp[x][y] = dp[x-1][y-1] + 1
        else:
            dp[x][y] = max(dp[x-1][y], dp[x][y-1])
            
print(dp[i][j])