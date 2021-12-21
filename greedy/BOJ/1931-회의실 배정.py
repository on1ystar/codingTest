import sys
import operator
N= int(input())
meetings = []
for _ in range(N):
    meetings.append(tuple(map(int, sys.stdin.readline().split())))
# sorted_meetings_by_start = sorted(dict.items(), key=operator.itemgetter(0))  # by values
sorted_meetings_by_end = list(sorted(meetings, key=operator.itemgetter(1)))  # by ends
pre_meeting = sorted_meetings_by_end[0]
# start_index = 0
end_index = 1
result = 1
#   가장 작은 end를 가지고 있는 회의 중 start가 이전 회의보다 큰 회의
while end_index < len(sorted_meetings_by_end):
    if sorted_meetings_by_end[end_index][0] >= pre_meeting[1]:
        pre_meeting = sorted_meetings_by_end[end_index]
        result += 1
    end_index += 1
print(result)