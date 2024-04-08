def solution(numbers, hand):

    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11

    left = 10
    right = 12
    li = []
    l_side = [1, 4, 7, 10]
    r_side = [3, 6, 9, 12]
    center = [2, 5, 8, 11]
    for i in numbers:
        if i in l_side:
            left = i
            li.append('L')
        elif i in r_side:
            right = i
            li.append('R')
        else:
            if left in center:
                left_dis = abs(center.index(i) - center.index(left))
            else:
                left_dis = abs(l_side.index(i-1) - l_side.index(left)) + 1
            if right in center:
                right_dis = abs(center.index(i) - center.index(right))
            else:
                right_dis = abs(r_side.index(i+1) - r_side.index(right)) + 1

            if left_dis < right_dis:
                left = i
                li.append('L')
            elif left_dis > right_dis:
                right = i
                li.append('R')
            else:
                if hand == 'right':
                    right = i
                    li.append('R')
                else:
                    left = i
                    li.append('L')

    return ''.join(i for i in li)