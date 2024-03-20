def solution(numbers, k):
    numbers.extend(numbers)
    arr = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
    k %= len(arr)
    return arr[k - 1]