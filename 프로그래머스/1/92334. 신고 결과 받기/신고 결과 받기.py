def solution(id_list, report, k):
    score = {v: 0 for i, v in enumerate(id_list)}
    blowers = {v: set() for i, v in enumerate(id_list)}

    for i in report:
        blower, reported = i.split()[0], i.split()[1]
        if reported not in blowers[blower]:
            blowers[blower].add(reported)
            score[reported] += 1

    banned = [i for i in score.keys() if score[i] >= k]

    answer = []
    for i in range(len(id_list)):
        cnt = 0
        for j in banned:
            if j in blowers[id_list[i]]:
                cnt += 1
        answer.append(cnt)

    return answer