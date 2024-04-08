def solution(data, ext, val_ext, sort_by):
    info = ['code', 'date', 'maximum', 'remain']
    idx = info.index(ext)
    sort_idx = info.index(sort_by)

    answer = []
    for i in data:
        if i[idx] < val_ext:
            answer.append(i)

    return sorted(answer, key=lambda x: x[sort_idx])