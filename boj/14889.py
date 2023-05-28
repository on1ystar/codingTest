# 스타트와 링크

from itertools import combinations

if __name__ == "__main__":
    N = int(input())
    S = []
    for _ in range(N):
        S.append(list(map(int, input().split())))
    sum_S = sum(S)
    min_diff = 1000
    team_start_list = list(combinations(range(N), N//2))
    for team_start in team_start_list[:len(team_start_list)//2]:
        team_start_stat, team_link_stat = 0, 0
        team_link = list(set(range(N)) - set(team_start))
        for i in team_start:
            for j in team_start:
                team_start_stat += S[i][j]
        for i in team_link:
            for j in team_link:
                team_link_stat += S[i][j]
        min_diff = min(min_diff, abs(team_start_stat - team_link_stat))
    print(min_diff)