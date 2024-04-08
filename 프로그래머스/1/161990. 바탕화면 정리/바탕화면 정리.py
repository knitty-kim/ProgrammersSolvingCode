def solution(wallpaper):
    info = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                info.append((i, j))
                info.append((i+1, j+1))
    lux = min(info)[0]
    rdx = max(info)[0]

    info = sorted(info, key=lambda x: x[1])
    luy = info[0][1]
    rdy = info[-1][1]

    return [lux, luy, rdx, rdy]