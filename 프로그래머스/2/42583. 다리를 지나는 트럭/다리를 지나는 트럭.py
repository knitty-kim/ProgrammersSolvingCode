def solution(bridge_length, weight, truck_weights):
    done = []
    bridge = []
    aging_truck = [[i, 0] for i in truck_weights]

    sec = 0
    while len(done) < len(truck_weights):
        # 경과시간 처리
        sec += 1

        # 다리 위 트럭들 에이징 처리
        if bridge:
            for i in bridge:
                i[1] += 1

        if len(bridge) <= bridge_length:
            # 대기 트럭 한 대 뽑기
            if aging_truck:
                temp = aging_truck[0]
            if bridge and bridge[0][1] == bridge_length:
                done.append(bridge.pop(0))
            if sum(i[0] for i in bridge) + temp[0] <= weight:
                if aging_truck:
                    bridge.append(aging_truck.pop(0))


    return sec