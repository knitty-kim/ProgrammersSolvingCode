def solution(array):
    answer = []
    answer.append(max(array))
    for i in range(len(array)):
        if answer[0] == array[i]:
            answer.append(i)
    return answer