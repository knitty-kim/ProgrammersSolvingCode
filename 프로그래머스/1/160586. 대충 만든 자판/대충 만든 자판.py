def solution(keymap, targets):
    # 기록지 초기화
    record = dict()
    for i in targets:
        for ch in i:
            record[ch] = 101

    # 기록지 갱신
    for i in keymap:
        for j in i:
            if j in record:
               record[j] = min(record[j], i.find(j)+1)

    for key in record.keys():
        if record[key] == 101:
            record[key] = -1

    # 결과 갱신
    answer = [0] * len(targets)
    for i, v in enumerate(targets):
        count = 0
        for j in v:
            if j in record:
                if record[j] != -1:
                    count += record[j]
                else:
                    count = record[j]
                    break
        answer[i] = count

    return answer