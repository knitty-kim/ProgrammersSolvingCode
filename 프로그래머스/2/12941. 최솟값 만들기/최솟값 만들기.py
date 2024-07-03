def solution(A,B):
    answer = 0
    
    # 1. 각각 오름차순, 내림차순 정렬
    A.sort(reverse=True)
    B.sort()
    
    # 2. 순회하면서 곱한 값을 answer에 더하기
    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer