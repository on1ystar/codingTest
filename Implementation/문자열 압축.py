def solution(s):
    max_slice_len = len(s) // 2
    slice_len = 1
    min_compression_len = len(s)
    while slice_len <= max_slice_len:
        pre_slice = ""
        duplicate_cnt = 1
        compression_s = ""
        for i in range(0,len(s),slice_len):
            if i+slice_len <= len(s):
                now_slice = s[i:i + slice_len]
                if pre_slice == "":
                    pre_slice = now_slice
                elif pre_slice == now_slice:
                    duplicate_cnt += 1
                else:
                    if duplicate_cnt != 1:
                        compression_s += str(duplicate_cnt) + pre_slice
                    else:
                        compression_s += pre_slice
                    pre_slice = now_slice
                    duplicate_cnt = 1
            else:
                pre_slice += s[i:]
        if duplicate_cnt != 1:
            compression_s += str(duplicate_cnt) + pre_slice
        else:
            compression_s += pre_slice
        if min_compression_len > len(compression_s):
            min_compression_len = len(compression_s)
        slice_len += 1
    return min_compression_len

print(solution("xababcdcdababcdcd"))