def solution(my_string):
    return sum([int(i) for i in my_string if 49 <= ord(i) <= 57])