n, m = list(map(int, input().split()))
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

dp = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = a[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j - 1] + a[i][j]
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + a[i][j]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + a[i][j]

print(dp[n - 1][m - 1])
