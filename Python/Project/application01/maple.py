import urllib.request
from urllib import parse
from bs4 import BeautifulSoup

while True:
    nickname = input('닉네임을 입력하세요 > ')
    input_Encoded = parse.quote(nickname)
    url = 'https://maple.gg/u/'+ input_Encoded
    req = urllib.request.urlopen(url) 
    res = req.read() 

    soup = BeautifulSoup(res,'html.parser') 
    name = soup.find('b',class_='align-middle')
    exp = soup.find('div',class_='user-summary')
    ranking = soup.find('div',class_='row row-normal user-additional')
    무릉 = soup.find('h1',class_='user-summary-floor font-weight-bold')
    시간 = soup.find('small',class_='user-summary-duration')


    print('닉네임 : ',name.get_text())
    print('직업 : ',exp.get_text().split()[1])
    print('레벨(경험치) : ',exp.get_text().split()[0])
    print('인기도 : ',exp.get_text().split()[3])
    print('길드 : ',ranking.get_text().split()[1])
    print('월드랭킹 : ',ranking.get_text().split()[5])
    print('무릉 층수(기록)',무릉.get_text().split()[0],'층 (',시간.get_text().split()[0],시간.get_text().split()[1],')')
