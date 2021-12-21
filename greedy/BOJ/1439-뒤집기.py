S = input()
currnet_str = S[0]
bundle_counts = [0, 0]
bundle_counts[int(currnet_str)] += 1
for next_str in S[1:]:
    if currnet_str != next_str:
        currnet_str = next_str
        bundle_counts[int(currnet_str)] += 1
print(min(bundle_counts[0], bundle_counts[1]))