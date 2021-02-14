def solution(s):
    max_slice_len = len(s) // 2
    slice_len = 1
    min_compression_len = len(s)
    while slice_len <= max_slice_len:
        pre_slice = ""
        duplicate_cnt = 1
        compression_s = ""
        for i in range(0,len(s),slice_len):  # s 인덱스를 slice_len 만큼 건너 뛰면서
            if i+slice_len <= len(s):  # s 인덱스 초과 검사
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
            else:  # s 인덱스 초과 시 남은 자투리 문자열 합치기
                now_slice = pre_slice + s[i:]
        if duplicate_cnt != 1:
            compression_s += str(duplicate_cnt) + now_slice
        else:
            compression_s += now_slice
        if min_compression_len > len(compression_s):
            min_compression_len = len(compression_s)
        slice_len += 1
    return min_compression_len

print(solution("xababcdcdababcdcd"))