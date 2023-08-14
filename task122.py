n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    j = i - 1
    while j >= 0:
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        j -= 1

print(max(dp))
