N, M, K = list(map(int, input().split()))
nums = list(map(int, input().split()))
result = 0
nums.sort(reverse=True)
result = nums[0] * K *(M // K) + nums[1] * (M % K)
print(result)
