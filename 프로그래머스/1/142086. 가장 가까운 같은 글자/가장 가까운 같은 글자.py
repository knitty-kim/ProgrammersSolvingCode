def solution(s):
    li = []
    answer = ''
    for i in range(len(s)):
        if answer.find(s[i]) == -1:
            li.append(-1)
            answer += s[i]
        else:
            li.append(i - (len(answer) - answer[-1::-1].index(s[i]) - 1))
            answer += s[i]
    return li