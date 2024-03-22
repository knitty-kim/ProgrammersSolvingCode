def solution(A, B):

    # 최대 (A 길이 - 1)만큼 회전
    for i in range(len(A)):
        if A == B:
            return i
        a = A[len(A)-1]
        A = a + A[:len(A)-1]
        print(A)
    return -1