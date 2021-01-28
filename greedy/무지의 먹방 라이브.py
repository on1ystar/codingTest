def solution(food_times, k):
    answer = 0
    while answer == 0:
        n = k // len(food_times)
        cnt = k % len(food_times)
        over = 0
        for i, x in enumerate(food_times):
            if (x - n) < 0:
                over += x*(-1)
                food_times[i] = 0
            elif (x - n) == 0:
                food_times[i] = 0
                cnt -= 1
            else:
                food_times[i] -= n
                cnt -= 1
            if cnt == 0:
                answer = i
                break
        k = cnt + over
    return answer
