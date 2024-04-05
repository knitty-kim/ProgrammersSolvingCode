def solution(board, h, w):
    color = board[h][w]
    info = list()
    for (i, j) in [(h, w - 1), (h, w + 1), (h - 1, w), (h + 1, w)]:
        if 0 <= i <= len(board)-1 and 0 <= j <= len(board)-1:
            if board[i][j] == color:
                info.append((i, j))

    return len(info)