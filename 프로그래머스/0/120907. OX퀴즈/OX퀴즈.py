def solution(quiz):
    li = [i.split(' = ') for i in quiz]
    answer = []
    for i in li:
        if eval(i[0]) == int(i[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer