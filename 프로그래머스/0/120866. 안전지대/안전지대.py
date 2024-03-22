def solution(board):
    map_dic = {(i, j): 0 for i in range(len(board)) for j in range(len(board))}

    for row_idx in range(len(board)):
        for col_idx in range(len(board[row_idx])):
            if board[row_idx][col_idx] == 1:
                map_dic[(row_idx, col_idx)] = 1
                map_dic[(row_idx-1, col_idx)] = 1
                map_dic[(row_idx+1, col_idx)] = 1
                map_dic[(row_idx, col_idx-1)] = 1
                map_dic[(row_idx, col_idx+1)] = 1
                map_dic[(row_idx-1, col_idx-1)] = 1
                map_dic[(row_idx-1, col_idx+1)] = 1
                map_dic[(row_idx+1, col_idx-1)] = 1
                map_dic[(row_idx+1, col_idx+1)] = 1

    return sum(1 for i in map_dic.keys() if map_dic[i] == 0)