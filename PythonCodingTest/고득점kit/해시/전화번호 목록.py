# # 인덱스로 비교
def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer


# sort하고, zip, startswith 함수 사용
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

# # hash 이용하기
def solution(phone_book):
    answer = True
    hash_map = {}
    #   전화번호 번째 방에 1을 넣어주기
    for phone_number in phone_book:
        hash_map[phone_number] = 1


    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer