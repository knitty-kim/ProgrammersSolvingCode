def solution(bandage, health, attacks):
    skill_t, heal, plus_heal = bandage[0], bandage[1], bandage[2]
    heal_cnt = 0
    limit_health = health
    end_t = max(attacks)[0]
    atck_dic = {i[0]: i[1] for i in attacks}
    
    for i in range(0, end_t+1):
        # 몬스터 공격 받으면 -체력, 연속성공cnt 초기화
        if i in atck_dic:
            health -= atck_dic[i]
            heal_cnt = 0
            if health <= 0:
                return -1
        # 몬스터 공격 안받으면 +체력, 연속성공cnt+1
        else:
            heal_cnt += 1
            # 연속성공cnt == 기술시전시간이면 추가체력회복, 연속성공cnt 초기화
            if heal_cnt == skill_t:
                health += heal
                health += plus_heal
                if health > limit_health:
                    health = limit_health
                heal_cnt = 0
            # 연속성공cnt != 기술시전시간이면 +체력, 연속성공cnt+1
            else:
                health += heal
                if health > limit_health:
                    health = limit_health

    return health