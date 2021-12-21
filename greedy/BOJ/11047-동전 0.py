N, K = map(int, input().split())
coins = []
result = 0
for _ in range(N):
    coins.append(int(input()))
for coin in coins[-1:0:-1]:
    result += K // coin
    K %= coin
print(result + K)