# from sys import stdin
#
# n, k = map(int, input().rstrip().split())
# coins = []
# dp = [0] * (k+1)
# for _ in range(n):
#     coin = int(stdin.readline().rstrip())
#     coins.append(coin)
# for i in range(1, k+1):
#     temp = []
#     for coin in coins:
#         if 0 < (i - coin):
#             if dp[i - coin] != 0:
#                 temp.append((i - coin, dp[i - coin]))
#         elif (i - coin) == 0:
#             dp[i] += 1
#     print(temp)
# print(dp[k])