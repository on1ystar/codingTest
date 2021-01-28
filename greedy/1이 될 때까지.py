n, k = map(int, input().rstrip().split())
cnt = 0
while n > 2:
    if n % k == 0:
        n //= k
        cnt += 1
    else:  # 한 번에 뺴는 식으로 개선할 수 있음
        n -= 1
        cnt += 1
print(cnt)