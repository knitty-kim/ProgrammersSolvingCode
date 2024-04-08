def solution(board, moves):
    result = []
    cnt = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                result.append(board[j][i-1])
                board[j][i-1] = 0

                if len(result) > 1:
                    if result[-1] == result[-2]:
                        result.pop()
                        result.pop()
                        cnt += 2
                break

    return cnt