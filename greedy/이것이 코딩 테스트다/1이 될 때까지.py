n, K = map(int, input().split())
rest = 0
result = 0
while(n >= K):
    if n % K != 0:
        rest = n % K
        n -= rest
        result += rest
    n //= K
    result += 1
result += n - 1
print(result)