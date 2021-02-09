from math import ceil

N, M = map(int, input().rstrip().split())
rice_cakes = list(map(int, input().rstrip().split()))
rice_cakes.sort()
start = 0
end = N - 1
while start <= end:
    mid = (start + end) // 2
    h = rice_cakes[mid]
    sum_rc = 0
    for rice_cake in rice_cakes[mid+1:]:
        sum_rc += (rice_cake - h)
    if sum_rc == M:
        break
    elif sum_rc > M:
        start = mid + 1
    else:
        end = mid - 1
if sum_rc == M:
    print(h)
elif sum_rc < M:
    k = ceil((M - sum_rc) / (N-mid))
    print(h - k)
elif sum_rc > M:
    k = ceil((sum_rc - M) / (N-mid))
    print(h +  k)
