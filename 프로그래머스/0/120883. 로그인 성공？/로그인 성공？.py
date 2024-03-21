def solution(id_pw, db):
    tmp_dic = dict(i for i in db)
    # print(tmp_dic)

    for i in tmp_dic:
        if id_pw[0] not in tmp_dic:
            # print('fail')
            return "fail"
        else:
            if id_pw[1] == tmp_dic[id_pw[0]]:
                return "login"
                # print('login')
            else:
                # print('wrong pw')
                return "wrong pw"