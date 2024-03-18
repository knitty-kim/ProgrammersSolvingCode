def solution(array, height):
    for i in array[:]:
        if i <= height:
            array.remove(i)
    return len(array)