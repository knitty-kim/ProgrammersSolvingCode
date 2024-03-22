def solution(quiz):
    li = [i.split(' = ') for i in quiz]
    answer = []
    for i in li:
        if ' - ' in i[0]:
            tmp_li = i[0].split(' - ')
            if int(i[1]) == (int(tmp_li[0]) - int(tmp_li[1])):
                answer.append('O')
            else:
                answer.append('X')
        elif ' + ' in i[0]:
            if int(i[1]) == sum(int(j) for j in i[0].split(' + ')):
                answer.append('O')
            else:
                answer.append('X')
    return answer