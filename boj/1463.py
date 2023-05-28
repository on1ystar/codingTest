n = int(input())
dp = [0] * (n+1)
for i in range(2, n+1):
    temp = []
    for x in range(2,4):
        if i % x == 0:
            temp.append(1 + dp[i // x])
        else:
            temp.append(1 + dp[i - 1])
    dp[i] = min(temp)
print(dp[n])