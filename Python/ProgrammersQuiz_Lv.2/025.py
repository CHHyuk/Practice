# [1차] 뉴스 클러스터링 xxxxxxxxxxxx
 
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    list1,list2 = [],[]
    temp1,temp2 = [],[]
    a = 0
    b = 0
    for x in range(1,len(str1)):
        list1.append(str1[x-1]+str1[x])
    for y in range(1,len(str2)):
        list2.append(str2[y-1]+str2[y])
     
    for i in list1:
        if i.isalpha():
            temp1.append(i)
        else:
            pass
    
    for i in list2:
        if i.isalpha():
            temp2.append(i)
        else:
            pass
    temp1 = list(set(temp1))
    temp2 = list(set(temp2))

    for i in range(len(temp2)):
        if temp2[i] in temp1:
            a += 1
        else:
            b += 1
    b += len(temp1)
    
    if b == 0:
        return 0
    else:
        return int((a/b) * 65536)
            




solution("aa1+aa2","AAAA12")