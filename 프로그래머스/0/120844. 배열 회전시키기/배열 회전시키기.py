def solution(numbers, direction):
    if len(direction) == 4:
        numbers.append(numbers[0])
        numbers.remove(numbers[0])
    else:
        numbers.insert(0, numbers[-1])
        numbers.pop()
    return numbers