def solution(park, routes):
    x, y = 0, 0
    clog_li = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = i, j
            elif park[i][j] == 'X':
                clog_li.append((i, j))

    for i in routes:
        oper, dist = i[0], int(i[-1])
        nx, ny = x, y
        for j in range(1, dist+1):
            dx, dy = 0, 0
            if oper == 'E':
                dy += 1
            elif oper == 'W':
                dy -= 1
            elif oper == 'S':
                dx += 1
            elif oper == 'N':
                dx -= 1
            if (nx+dx, ny+dy) not in clog_li:
                if 0 <= nx+dx <= len(park)-1 and 0 <= ny+dy <= len(park[0])-1:
                    nx, ny = nx+dx, ny+dy
                else:
                    nx, ny = x, y
                    break
            else:
                nx, ny = x, y
                break
        x, y = nx, ny
    return [x, y]