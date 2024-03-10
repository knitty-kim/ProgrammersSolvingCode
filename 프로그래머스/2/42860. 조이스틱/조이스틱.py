def solution(name):
    # 조이스틱 조작 횟수
    answer = 0

    # 기본 최소 좌우 이동 횟수 = 길이 -1
    min_move = len(name) - 1

    for i, char in enumerate(name):
        # 현재 위치에서의 위 아래 최소 조작
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 현재 위치 이후, 연속된 A 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    answer += min_move
    return answer