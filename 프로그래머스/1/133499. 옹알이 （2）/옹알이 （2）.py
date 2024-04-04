def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    number = ['1', '2', '3', '4']
    banned = ['11', '22', '33', '44']

    count = 0
    for i in range(len(babbling)):
        for j, word in enumerate(words):
            babbling[i] = babbling[i].replace(word, number[j])
            if babbling[i].isdigit():
                for ban in banned:
                    if ban in babbling[i]:
                        break
                else:
                    count += 1
                    break

    return count