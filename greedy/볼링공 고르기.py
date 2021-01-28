import collections
import math

n, m  = map(int, input().rstrip().split())
li = list(map(int, input().rstrip().split()))
result = math.factorial(n) // (math.factorial(n-2)*2)
count = collections.Counter(li)
for i in range(1, m+1):
    n = count[i]
    if n == 1 or n == 0:
        continue
    if n == 2:
        result -= 1
        continue
    result -= math.factorial(n) // math.factorial(n-2)*2
print(result)

