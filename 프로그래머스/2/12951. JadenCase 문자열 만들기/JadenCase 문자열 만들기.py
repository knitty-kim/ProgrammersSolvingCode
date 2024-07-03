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
        if start == end:
            answer += ' '
            start += 1
            continue
        if end == len(s)-1:
            break
        element = s[start:end]
        if element[0].islower():
            answer += element[0].upper() + element[1:].lower() + ' '
        else:
            answer += element[0] + element[1:].lower() + ' '
        
        start = end+1
    
    
    if s[start].islower():
        answer += s[start].upper() + s[start+1:].lower()
    else:
        answer += s[start] + s[start+1:].lower()
          
    return answer