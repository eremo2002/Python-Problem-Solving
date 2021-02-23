n = int(input())

# dp[i][j] : i, j에 도착했을 때 최대값
arr = [[0]*(n+1) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n)]

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        arr[i][j+1] = tmp[j]

dp[0][1] = arr[0][1]

for i in range(1, n):
    for j in range(1, n+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

print(max(dp[-1]))
