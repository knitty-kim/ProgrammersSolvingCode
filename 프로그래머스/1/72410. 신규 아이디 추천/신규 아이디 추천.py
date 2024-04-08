def solution(new_id):
    recommend = new_id.lower()
    result = []

    for i in recommend:
        if i.isalnum() or i in ['-', '_', '.']:
            result.append(i)
            if len(result) > 1:
                if result[-2] == '.' and result[-1] == '.':
                    result.pop()
    if result[-1:] == ['.']:
        result.pop()
    if result[0::-1] == ['.']:
        result.pop(0)

    pre = ''
    if len(result) == 0:
        pre += 'a'
    else:
        pre = ''.join(i for i in result)

    if len(pre) >= 16:
        pre = pre[:15]
    elif len(pre) <= 2:
        while True:
            pre += pre[-1]
            if len(pre) == 3:
                break

    if pre[-1:] == '.':
        pre = pre[:len(pre)-1]
    elif pre[0::-1] == '.':
        pre = pre[1::]
        
    return pre