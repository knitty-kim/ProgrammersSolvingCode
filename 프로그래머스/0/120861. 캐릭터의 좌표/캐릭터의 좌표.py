def solution(keyinput, board):
    verti = 0
    hori = 0

    for i in keyinput:
        if i == "up" and verti < (board[1]-1) // 2:
            verti += 1
        elif i == "down" and verti > -(board[1]-1) // 2:
            verti -= 1
        elif i == "right" and hori < (board[0]-1) // 2:
            hori += 1
        elif i == "left" and hori > -(board[0]-1) // 2:
            hori -= 1

    return [hori, verti]