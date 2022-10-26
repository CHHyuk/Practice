# List와 문자열
    # 리스트와 문자열은 유사하다
    # 서로 변환이 가능하다
    # list = str.split() : 문자열에서 리스트로
    # " ".join(list) : 리스트에서 문자열로

characters = list('abcdef')
print(characters)

words = "나는 장한혁 입니다. 파이썬을 배우고 있습니다."
words_list = words.split()
print(words_list)

math = '12+25+30'
math_list = math.split("+")
print(math_list)

print("+".join(math_list))


print(" ".join(words_list))

