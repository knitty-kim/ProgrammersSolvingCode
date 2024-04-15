def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        cnt = 0
        if progresses[0] >= 100:
            for i in progresses:
                if i >= 100:
                    cnt += 1
                else:
                    break
            if cnt != 0:
                progresses = progresses[cnt:]
                speeds = speeds[cnt:]
                answer.append(cnt)

    return answer