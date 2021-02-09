N, x = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
def binary_search():
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return False

cnt = 1
if not binary_search():
    print(-1)
else:
    i = binary_search()
    under = i - 1
    while under >= 0:
        if nums[under] == x:
            cnt += 1
            under -= 1
        else: break
    upper = i + 1
    while upper <= N-1:
        if nums[upper] == x:
            cnt += 1
            upper += 1
        else: break
    print(cnt)
