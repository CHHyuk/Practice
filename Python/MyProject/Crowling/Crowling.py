import urllib.request #원하는 사이트에 접속하는 것
from bs4 import BeautifulSoup #접속한 페이지의 모든 값을 가져오는 것

url = 'https://www.naver.com/'
req = urllib.request.urlopen(url) # url에 대한 연결 요청
res = req.read() # 연결요청에 대한 응답

soup = BeautifulSoup(res,'html.parser') # BeautifulSoup 객체 생성
keywords = soup.find_all('div',class_='chart_view_wrap type_music') # 데이터에서 태그와 클래스를 찾는 함수

keywords = [each_line.get_text().strip() for each_line in keywords[:20]]
#get_text() == 데이터에서 문자열만 추출
#strip() == 데이터의 양옆 공백제거
print(keywords)
