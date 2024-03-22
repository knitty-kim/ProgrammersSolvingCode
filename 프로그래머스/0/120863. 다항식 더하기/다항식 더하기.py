def solution(polynomial):
    li = list(polynomial.split(' + '))

    num_li = [i for i in li if i.isdigit()]
    x_li = [i for i in li if i not in num_li]

    answer = ''
    sum_x = sum(int(i[:-1]) if not i.isalpha() else 1 for i in x_li)
    sum_num = sum(int(i) for i in num_li)

    if sum_x > 0:
        if sum_x == 1:
            answer += 'x'
        else:
            answer += str(sum_x) + 'x'
        if sum_num > 0:
            answer += ' + ' + str(sum_num)
    elif sum_x == 0:
        answer += str(sum_num)

    return answer