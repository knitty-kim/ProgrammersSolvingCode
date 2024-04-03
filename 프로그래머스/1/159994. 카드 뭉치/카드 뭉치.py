def solution(cards1, cards2, goal):
    copy_goal = list(i for i in goal)
    for i in goal:
        if i in cards1 and cards1.index(i) == 0:
            cards1.remove(i)
            copy_goal.remove(i)
        elif i in cards2 and cards2.index(i) == 0:
            cards2.remove(i)
            copy_goal.remove(i)
        else:
            return "No"

    if len(cards1) == 0 and len(cards2) == 0:
        return 'Yes'
    elif len(copy_goal) == 0:
        return "Yes"
    else:
        return "No"