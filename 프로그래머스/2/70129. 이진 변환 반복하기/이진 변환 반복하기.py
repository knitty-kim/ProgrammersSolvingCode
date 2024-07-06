def solution(s):
    count_bin = 0
    count_zero = 0
    
    answer = [0, 0]
    
    while True:
        if s == '1':
            break
        temp = ''
        for i in range(len(s)):
            if s[i] == '0':
                count_zero += 1
            else:
                temp += s[i]
        s = format(len(temp), 'b')
        count_bin += 1
        
        
    answer[0] = count_bin
    answer[1] = count_zero
    
    return answer