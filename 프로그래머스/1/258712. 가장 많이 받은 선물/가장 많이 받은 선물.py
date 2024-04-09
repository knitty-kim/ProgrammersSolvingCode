def solution(friends, gifts):
    # 선물지수
    dic = {i: 0 for i in friends}
    # 인덱스 기록지
    info = {v: i for i, v in enumerate(friends)}
    # 명월예측지
    next_predict = list([0 for _ in range(len(friends))] for _ in range(len(friends)))

    for i in gifts:
        # 선물지수 갱신
        giver, receiver = i.split()[0], i.split()[1]
        dic[giver] += 1
        dic[receiver] -= 1
        # 명월예측지 갱신
        next_predict[info[giver]][info[receiver]] += 1

    cnt = 0
    for i in range(len(next_predict)):
        temp_cnt = 0
        for j in range(len(next_predict)):
            if i != j:
                if next_predict[i][j] > next_predict[j][i]:
                    temp_cnt += 1
                elif next_predict[i][j] == next_predict[j][i]:
                    if dic[friends[i]] > dic[friends[j]]:
                        temp_cnt += 1
        cnt = max(cnt, temp_cnt)

    return cnt