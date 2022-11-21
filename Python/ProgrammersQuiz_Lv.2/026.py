# 전화번호 목록 xxxxxxxxxxxxxxxxx

def solution(phone_book):
    check = 0
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if phone_book[i][0] != phone_book[j][0]:
                if int(phone_book[i][0]) > int(phone_book[j][0]):
                    continue
                else:
                    break
            elif i == j:
                continue
            elif len(phone_book[i]) <= len(phone_book[j]) and phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                check += 1
                break

    if check == 0:
        return True
    else:
        return False

        
                











solution(["12","123","1235","567","88",'124','1166'])