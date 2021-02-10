from sys import stdin

N, C = map(int, input().rstrip().split())
house = []
for _ in range(N):
    house.append(int(stdin.readline().rstrip()))
house.sort()
min_d = 1
max_d = house[-1] - house[0]
finded_min_d = 0
while min_d <= max_d:
    mid_d = (min_d + max_d) // 2
    now_house = house[0]
    wifi_cnt = 1
    for next_house in house[1:]:
        wifi_d = next_house - now_house
        if wifi_d >= mid_d:
            wifi_cnt += 1
            now_house = next_house
    if wifi_cnt >= C:
        finded_min_d = mid_d
        min_d = mid_d + 1
    else:
        max_d = mid_d - 1
print(finded_min_d)