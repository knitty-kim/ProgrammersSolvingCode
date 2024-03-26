def solution(arr1, arr2):
    return [[a+b for a, b in zip(*x)] for x in zip(arr1, arr2)]