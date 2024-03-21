def solution(id_pw, db):
    # tmp_dic = dict(i for i in db)
    tmp_dic = dict(db)

    for _ in tmp_dic:
        if id_pw[0] not in tmp_dic:
            return "fail"
        else:
            if id_pw[1] == tmp_dic[id_pw[0]]:
                return "login"
            else:
                return "wrong pw"