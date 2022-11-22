def get_web(url): # URL을 넣으면 페이지 내용을 가져오는 함수
    import urllib.request # urllib 라이브러리 가져와서
    response = urllib.request.urlopen(url) # 받은 url을 열고
    data = response.read() # 데이터를 읽어서
    decoded = data.decode('utf-8') # 사람이 읽을 수 있게 디코딩하고
    return decoded # 돌려주는 함수

url = input('웹 페이지 주소? ')
content = get_web(url)
print(content)