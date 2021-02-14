N = int(input())
warehouse = [0] + list(map(int, input().rstrip().split()))
dp = [0] * (N + 1)
dp[1], dp[2] = warehouse[1], warehouse[2]
for i in range(3, N+1):
    dp[i] = warehouse[i] + max(dp[i-2], dp[i-3])
print(max(dp[-1], dp[-2]))
