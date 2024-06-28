def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 새 자물쇠 생성 = 기존 자물쇠 3배
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # 새 자물쇠 가운데에 기존 자물쇠 초기화
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    # 4가지 방향에 대한 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
                # 3배 자물쇠에 열쇠 꽂기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 새 자물쇠에 열쇠가 맞는지 체크
                if check(new_lock) == True:
                    return True
                # 3배 자물쇠에서 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False