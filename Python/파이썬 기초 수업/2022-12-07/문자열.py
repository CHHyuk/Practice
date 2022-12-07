# 문제 : string1을 구성하는 문자 중에서 a,b,c,d,e 를 제외하고 출력해주세요.
# 조건 : 함수로 만들고 실행해주세요.
# 조건 : 함수 안에 `string1 = "안a녕b하c세d요e"` 이 부분을 새로 넣어야 합니다.(지역변수로 만들어야 합니다)
# 조건 : 2개 이상 만들어주세요.

def sol_v1():
  string1 = "안a녕b하c세d요e" # string1의 길이는 10 이고 각각의 문자는, string1[0] 부터 string1[9] 까지 존재한다.

  rs = ""
  rs += string1[0] + string1[2] + string1[4] + string1[6] + string1[8]

  print(rs)

def sol_v2():
  string1 = "안a녕b하c세d요e"

  rs = ""

  string1_len = len(string1) # 문장의 길이
  i = 0

  while ( i < string1_len ):
    c = string1[i]
    if ( c != 'a' and c != 'b' and c != 'c' and c != 'd' and c != 'e' ):
      rs += c
    i += 1

  print(rs)

def sol_v3():
  string1 = "안a녕b하c세d요e"

  rs = ""

  for c in string1:
    if ( c != 'a' and c != 'b' and c != 'c' and c != 'd' and c != 'e' ):
      rs += c

  print(rs)

def sol_v4():
  string1 = "안a녕b하c세d요e"

  rs = ""

  for c in string1: # string1 안에 있는 문자 1개가 차례대로 c로 들어가서 실행된다. 반복횟수는 문장의 길이만큼이다.
    if c not in ['a', 'b', 'c', 'd', 'e']: # c안에 들어있는 문자와 a, b, c, d, e 중에 일치하는게 없다면
      rs += c

  print(rs)

sol_v1()
sol_v2()
sol_v3()
sol_v4()