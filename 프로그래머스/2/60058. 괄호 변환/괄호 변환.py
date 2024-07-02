# 괄호 변환

# 정확한 구현, 재귀 함수 구현 필요
# 코드 단순화 필요

# "균형잡힌 문자열"의 인덱스 반환
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# "올바른 문자열" 판단
def check_correct(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''

    # 1. 빈 문자열 반환
    if p == '':
        return answer

    # 2. u, v 분리
    idx = balanced_index(p)
    u = p[:idx+1]
    v = p[idx+1:]

    if check_correct(u):
        answer = u + solution(v)
    else:
        answer = "(" + solution(v) + ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)

    return answer