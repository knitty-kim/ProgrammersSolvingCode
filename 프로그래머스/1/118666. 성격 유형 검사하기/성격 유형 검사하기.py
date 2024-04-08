def solution(survey, choices):
    info = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    score = [3, 2, 1, 0, 1, 2, 3]
    for i in range(len(choices)):
        if choices[i] < 4:
            info[survey[i][0]] += score[choices[i]-1]
        elif choices[i] > 4:
            info[survey[i][1]] += score[choices[i]-1]

    answer = ''
    if info['R'] >= info['T']:
        answer += 'R'
    else:
        answer += 'T'
    if info['C'] >= info['F']:
        answer += 'C'
    else:
        answer += 'F'
    if info['J'] >= info['M']:
        answer += 'J'
    else:
        answer += 'M'
    if info['A'] >= info['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer