from collections import deque
def solution(s):
    answer = ''
    
    blank_li = []
    for i in range(len(s)):
        if s[i] == ' ':
            blank_li.append(i)
            
    blank_q = deque(blank_li)
    
    start = 0
    while blank_q:
        end = blank_q.popleft()
        if start == end:        # 현재 순회 중인 인덱스가 공백 문자 인덱스인 경우
            answer += ' '
            start += 1
            continue
        if end == len(s)-1:     # 공백 문자 인덱스가 끝인 경우
            # start == len(s)-1 상황과 동일
            break
        
        # 숫자 포함 알파벳 문자열 처리
        element = s[start:end]
        if element[0].islower():
            answer += element[0].upper() + element[1:].lower() + ' '
        else:
            answer += element[0] + element[1:].lower() + ' '
        
        start = end+1
    
    
    # 마지막 문자에 대한 처리
    if s[start].islower():
        answer += s[start].upper() + s[start+1:].lower()
    else:
        answer += s[start] + s[start+1:].lower()
          
    return answer