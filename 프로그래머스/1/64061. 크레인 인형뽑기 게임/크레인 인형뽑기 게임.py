def solution(board, moves):

    result = []
    cnt = 0
    dic = {i: [] for i in range(1, len(board)+1)}

    for i in range(len(board)):
        for j in range(len(board)):
            if j+1 in dic and board[i][j] != 0:
                dic[j+1].append(board[i][j])

    for i in moves:
        if len(dic[i]) > 0:
            result.append(dic[i].pop(0))
            if result[-2:-1] == result[-1:]:
                for _ in range(2):
                    result.pop()
                cnt += 2
    return cnt