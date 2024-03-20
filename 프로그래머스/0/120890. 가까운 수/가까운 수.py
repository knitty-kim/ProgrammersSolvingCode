def solution(array, n):
    array.sort(key=lambda x: (abs(x-n), x-n))
    return array[0]