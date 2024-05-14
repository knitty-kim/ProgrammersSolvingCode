def solution(operations):
    answer = []
    for i in operations:
        id, number = i.split()
        if id == 'I':
            answer.append(int(number))
        elif id == 'D' and len(answer) > 0:
            answer.sort()
            if number == '1':
                answer.pop()
            elif number == '-1':
                answer.pop(0)
    if len(answer) == 0:
        return [0, 0]
    else:
        answer.sort()
        return [answer[-1], answer[0]]