def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        temp_list = []
        for j in range(n):
            temp_list.append(num_list[i+j])
        answer.append(temp_list)
    return answer