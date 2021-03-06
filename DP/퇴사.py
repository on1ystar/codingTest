# 퇴사

# from sys import stdin
# n = int(stdin.readline().rstrip())
# tp = []
# dp = [0] * n
# for _ in range(n):
#     tp.append(list(map(int, stdin.readline().rstrip().split())))
# for i in range(n):
#     temp = [0]
#     for j in range(i):
#         if i - j >= tp[j][0]:
#             temp.append(dp[j])
#     if n - i >= tp[i][0]:
#         dp[i] = tp[i][1] + max(temp)
#     else:
#         dp[i] = max(temp)
# print(max(dp))

def dfs(now_sche, sche_time, now_profit, sum_profit):
    global max_profit
    end_sche = now_sche + sche_time
    if end_sche > n:
        max_profit = max(max_profit, sum_profit - now_profit)
        return
    max_profit = max(max_profit, sum_profit)
    for next_sche in range(end_sche, n):
        dfs(next_sche, schedule[next_sche][0], schedule[next_sche][1], sum_profit + schedule[next_sche][1])

if __name__ == "__main__":
    n = int(input())
    schedule = []
    max_profit = 0
    for _ in range(n):
        schedule.append(list(map(int, input().rstrip().split())))
    for start_day in range(n):
        dfs(start_day, schedule[start_day][0], schedule[start_day][1], schedule[start_day][1])
    print(max_profit)
    
