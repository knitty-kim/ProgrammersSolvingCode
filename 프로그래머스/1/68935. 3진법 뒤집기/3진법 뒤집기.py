def solution(n):
    # 3진법 - 각 자리수에 3의 x제곱을 합한 값
    answer = ''
    while n > 0:
        if n % 3 == 0:
            answer += '0'
        else:
            answer += str(n % 3)
        n //= 3

    # 문자열 뒤집기
    answer = answer[::-1]

    result = 0
    for i in range(len(answer)):
        result += int(answer[i]) * (3 ** i)
    return result