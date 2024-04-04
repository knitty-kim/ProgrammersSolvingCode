def solution(lottos, win_nums):
    prize = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    count = sum(1 for i in win_nums if i in lottos)
    return [prize[count+lottos.count(0)], prize[count]]