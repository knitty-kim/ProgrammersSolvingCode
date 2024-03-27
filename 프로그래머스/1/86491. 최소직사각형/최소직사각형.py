def solution(sizes):
    for i in sizes:
        i.sort(reverse=True)
    max_row = max(sizes)[0]
    max_col = max(sorted(i[1] for i in sizes))
    return max_row * max_col