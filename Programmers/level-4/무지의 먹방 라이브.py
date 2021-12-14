def solution(food_times, k):
    answer = 0
    rest_foods_cnt = len(food_times)
    rotation_times = k // rest_foods_cnt
    k %= rest_foods_cnt
    while rotation_times > 0:
        for i in range(len(food_times)):
            if food_times[i] <= 0: 
                continue
            if food_times[i] > rotation_times: 
                food_times[i] -= rotation_times
            else:
                k += rotation_times - food_times[i]
                food_times[i] = 0
                rest_foods_cnt -= 1
        if rest_foods_cnt == 0:
            answer = -1
            break
        rotation_times = k // rest_foods_cnt
        k %= rest_foods_cnt
    if answer != -1:
        for i in range(len(food_times)):
            if food_times[i] <= 0: continue
            else:
                if k == 0:
                    answer = i + 1
                    break
                k -= 1
    return answer

print(solution([1, 1000], 999))

# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#     answer = 0
#     food_times_dic = {}
#     for i, v in enumerate(food_times):
#         food_times_dic[i+1] = v
#     while True:
#         iter_cnt = k // len(food_times_dic)
#         if iter_cnt >= 1:
#             for key, time in list(food_times_dic.items()):
#                 temp = time - iter_cnt
#                 if temp <= 0:
#                     k -= iter_cnt + temp
#                     del food_times_dic[key]
#                 else:
#                     k -= iter_cnt
#                     food_times_dic[key] = temp
#         else:
#             answer = list(food_times_dic.items())[k][0]
#             break
#     return answer

# print(solution([3, 1, 2], 6))
