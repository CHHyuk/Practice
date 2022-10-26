dic = {'key2':'Value1'}

if 'key1' in dic and dic ['key1'] == 'value1': # 단락평가로 인해 and 뒤에 key1부분에서 에러가 안뜸
    print('key1도 있고 그 값은 value1이다')
else:
    print('아닙니다')

dic = {'key2':'Value1'}

if dic ['key1'] == 'value1' and 'key1' in dic: # 단락평가로 인해 key1이 없으므로 에러 발생
    print('key1도 있고 그 값은 value1이다')
else:
    print('아닙니다')