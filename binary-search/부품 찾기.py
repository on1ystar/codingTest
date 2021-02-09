N = int(input())
shop_parts = list(map(int, input().rstrip().split()))
M = int(input())
request_parts = list(map(int, input().rstrip().split()))
answer = []

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if shop_parts[mid] == target:
            return "yes"
        elif shop_parts[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return "no"


shop_parts.sort()
for parts in request_parts:
    answer.append(binary_search(parts, 0, N - 1))

print(' '.join(answer))
