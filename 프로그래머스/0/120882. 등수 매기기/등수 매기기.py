def solution(score):

    tmp_li = []
    for i in score:
        tmp_li.append((i[0] + i[1]) / 2)

    tmp_li2 = tmp_li[:]

    tmp_li.sort(reverse=True)
    tmp_dic = dict.fromkeys(tmp_li, 0)

    for i in range(len(tmp_li)):
        tmp_dic[tmp_li[i]] = i + 1
        if tmp_li.count(tmp_li[i]) != 1:
            tmp_dic[tmp_li[i]] -= tmp_li.count(tmp_li[i]) - 1

    answer = []
    for j in tmp_li2:
        if j in tmp_dic:
            answer.append(tmp_dic[j])

    # print(answer)
    # print(tmp_li2)
    # print(tmp_li)
    # print(tmp_dic)

    return answer