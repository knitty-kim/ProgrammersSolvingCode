def solution(phone_book):
    dic = {i: None for i in phone_book}
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in dic and temp != phone_number:
                return False
    return True