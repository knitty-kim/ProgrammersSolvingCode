def solution(phone_book):
    se = set(phone_book)
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in se and temp != phone_number:
                return False
    return True