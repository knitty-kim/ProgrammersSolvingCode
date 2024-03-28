def solution(array, commands):
    answer = []
    for i in commands:
        li = array[i[0]-1:i[1]]
        li.sort()
        answer.append(li[i[2]-1])
    return answer