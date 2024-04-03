def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]

    for i,v in enumerate(answers):
        if v == pattern1[i%len(pattern1)]:
            cnt[0] += 1
        if v == pattern2[i%len(pattern2)]:
            cnt[1] += 1
        if v == pattern3[i%len(pattern3)]:
            cnt[2] += 1
    return [i + 1 for i, v in enumerate(cnt) if v == max(cnt)]