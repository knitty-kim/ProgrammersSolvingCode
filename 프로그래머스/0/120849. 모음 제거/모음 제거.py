def solution(my_string):
    li = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for i in my_string:
        if i in li:
            continue
        else:
            answer += i

    return answer