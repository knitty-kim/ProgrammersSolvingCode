# 괄호 변환
from collections import deque
# 3. u 올바름 판단
def correct(u):
    if u[0] == '(':
        return True
    else:
        return False

def solution(p):
    count_l = 0
    count_r = 0
    queue = deque(list(p))
    # print(queue)
    u = ''
    v = ''
    while queue:
        c = queue.popleft()
        # print("뽑은 값 : " + c)
        # 1. 입력이 빈 문자열..
        if c == "":
            return ""
        # 2. u, v로 분리
        if c == '(':
            count_l += 1
            u += c
        else:
            count_r += 1
            u += c

        if count_l == count_r:
            while queue:
                v += queue.popleft()
            # print("u값 : " + u + ", v값 : " + v)

            if correct(u):
                u += solution(v)
            else:
                temp = "(" + solution(v) + ")"
                for i in u[1:len(u)-1]:
                    if i == '(':
                        temp += ')'
                    else:
                        temp += '('
                return temp

    return u




