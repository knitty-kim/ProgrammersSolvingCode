def solution(array):
    # 문자열 배열로 변환
    li = list(str(i) for i in array)
    # 하나의 문자열로 합치기
    stri = ''.join(li)
    # 문자 7의 개수 반환
    return stri.count('7')