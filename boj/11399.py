N = int(input())
p_list = []
p_list = list(map(int, input().rstrip().split()))
p_list.sort()
total_time = 0
temp = 0
for p in p_list:
    temp += p
    total_time += temp
print(total_time)
