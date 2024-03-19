def solution(my_string):
    answer = list(my_string)
    for i in range(len(my_string)):
        for j in range(i+1, len(my_string)):
            if my_string[i] == my_string[j]:
                answer[j] = ''
    return ''.join(answer)