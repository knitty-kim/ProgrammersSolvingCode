def solution(dartResult):
    zone = ['S', 'D', 'T']
    zone_opt = []
    for i, v in enumerate(dartResult):
        if v.isalpha():
            if dartResult[i+1:i+2] == '*':
                zone_opt.append((v, '*'))
            elif dartResult[i+1:i+2] == '#':
                zone_opt.append((v, '#'))
            else:
                zone_opt.append((v, ''))

    tmp_str = dartResult.replace('#', '')
    tmp_str = tmp_str.replace('*', '')
    for i in zone:
        tmp_str = tmp_str.replace(i, ' ')
    tmp_li = tmp_str.split()

    result = cal_number(tmp_li[0], zone_opt[0])
    for i in range(1, len(tmp_li)):
        bef = cal_number(tmp_li[i-1], zone_opt[i-1])
        number = cal_number(tmp_li[i], zone_opt[i])
        if zone_opt[i][1] == '*':
            result += (number + bef)
        else:
            result += number

    return result

def cal_number(number, zone_opt):
    zone = ['S', 'D', 'T']
    if zone_opt[1] == '*':
        return (int(number)**(zone.index(zone_opt[0]) + 1)) * 2
    elif zone_opt[1] == '#':
        return -int(number)**(zone.index(zone_opt[0]) + 1)
    else:
        return int(number)**(zone.index(zone_opt[0]) + 1)