N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

start = 0
end = N - 1
tri = 0
while start <= end:
    mid = (start + end) // 2
    if nums[mid] == mid:
        tri = 1
        print(mid)
        break
    elif nums[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1
if tri == 0: print(-1)
