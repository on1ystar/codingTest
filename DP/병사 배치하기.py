n = int(input())
soldier_power = [10000001] + list(map(int, input().rstrip().split())) + [0]
dp = [0] * (n+2)
i = 1
while i < (n+1):
    if not(soldier_power[i-1] >= soldier_power[i] >= soldier_power[i+1]):
        cnt_right = 1
        for j in range(i+1, n+2):
            if soldier_power[i - 1] >= soldier_power[j]:
                break
            cnt_right += 1
        cnt_left = 1
        for j in range(i-1, -1, -1):
            if soldier_power[j] >= soldier_power[i+1]:
                break
            cnt_left += 1
        dp[i+1] = min(cnt_left, cnt_right)
        i += dp[i+1]
    else:
        i += 1
print(dp)
print(sum(dp))
