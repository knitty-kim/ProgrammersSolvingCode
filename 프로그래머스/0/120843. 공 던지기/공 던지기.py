def solution(numbers, k):
    n = len(numbers)
    if n % 2 == 0:
        arr = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
        while k > len(arr):
            k %= len(arr)
        return arr[k-1]
    else:
        numbers.extend(numbers)
        arr2 = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
        while k > len(arr2):
            k %= len(arr2)
        return arr2[k - 1]