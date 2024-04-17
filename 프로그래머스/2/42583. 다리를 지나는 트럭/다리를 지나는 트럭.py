def solution(bridge_length, weight, truck_weights):
    done = []
    bridge = []
    aging_truck = [[i, 0] for i in truck_weights]

    sec = 0
    while len(done) < len(truck_weights):
        # 경과시간 처리
        sec += 1
        
        if len(bridge) <= bridge_length:
            if bridge:
            # 다리 위 트럭들 에이징 처리
                for i in bridge:
                    i[1] += 1
                if bridge[0][1] == bridge_length:
                    done.append(bridge.pop(0))
            # 대기 트럭 한 대 뽑기
            if aging_truck:
                temp = aging_truck[0]
                if sum(i[0] for i in bridge) + temp[0] <= weight:
                    bridge.append(aging_truck.pop(0))

    return sec