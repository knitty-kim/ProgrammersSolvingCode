def solution(emergency):
    # 배열을 내림차순으로 정렬
    li = sorted(emergency, reverse=True)

    # 정렬된 배열의 인덱스 + 1 = 응급도 순위
    # 원래 배열의 순서에 맞게 응급도 순위 매칭
    # 매칭된 배열을 return
    answer = [0] * len(li)
    for i in range(len(li)):
        answer[emergency.index(li[i])] = i + 1
    return answer