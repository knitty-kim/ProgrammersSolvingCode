def solution(answers):
    person1 = [1, 2, 3, 4, 5] * (len(answers)//5 + 5)
    person2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//8 + 8)
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10 + 10)

    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == person1[i]:
            cnt[0] += 1
        if answers[i] == person2[i]:
            cnt[1] += 1
        if answers[i] == person3[i]:
            cnt[2] += 1
    return [i+1 for i, v in enumerate(cnt) if v == max(cnt)]