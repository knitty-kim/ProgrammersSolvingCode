def solution(today, terms, privacies):
    dic = dict()
    result = []
    for i in terms:
        name, month = i.split()[0], i.split()[1]
        dic[name] = month

    for i in range(len(privacies)):
        dating, name = privacies[i].split()[0], privacies[i].split()[1]
        dating = dating.split('.')
        in_year, in_month, in_day = int(dating[0]), int(dating[1]), int(dating[2])
        new_year = str(in_year + (in_month + int(dic[name])) // 12)
        new_month = str((in_month + int(dic[name])) % 12)
        new_day = str((in_day + 27) % 28)
        if new_day == '0':
            new_day = '28'
            new_month = str(int(new_month) - 1)
        if new_month == '0':
            new_month = '12'
            new_year = str(int(new_year) - 1)
        if len(new_month) == 1:
            new_month = '0' + new_month
        if len(new_day) == 1:
            new_day = '0' + new_day
        new_dating = new_year + '.' + new_month + '.' + new_day
        if today > new_dating:
            result.append(i+1)

    return sorted(result)