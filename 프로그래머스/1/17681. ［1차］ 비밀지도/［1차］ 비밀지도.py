def solution(n, arr1, arr2):
    answer = list(list(format(i, 'b').zfill(n)) for i in arr1)
    arr2 = list(list(format(i, 'b').zfill(n)) for i in arr2)

    for i in range(len(arr2)):
        for j in range(len(arr2[i])):
            if arr2[i][j] == '1':
                answer[i][j] = '1'

    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
        answer[i] = answer[i].replace('1', '#')
        answer[i] = answer[i].replace('0', ' ')

    return answer