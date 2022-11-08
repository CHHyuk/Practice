import datetime
import urllib.request
from bs4 import BeautifulSoup
from time import sleep


now = datetime.datetime.now()
nowdate = now.strftime('%Y년 %m월 %d일')

url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%A3%BC%EC%8B%9D+%EC%B0%A8%ED%8A%B8&oquery=%EB%B9%84%ED%8A%B8%EC%BD%94%EC%9D%B8&tqi=h2Dv9sp0JywssD2d1NCssssstAV-238806'
req = urllib.request.urlopen(url) 
res = req.read()

soup = BeautifulSoup(res,'html.parser')
kos = soup.find_all('span','spt_con up')
Kos = [each_line.get_text().strip() for each_line in kos[:2]] # ['2,371.79  전일대비상승 23.36 (+0.99%)', '700.48  전일대비상승 6.59 (+0.95%)']
Dow = soup.find('li','up')
Dow = Dow.get_text().split() #['다우', '산업', '11.07.', '32,638.15', '전일대비', '상승', '234.93', '(+0.73%)']
Nas = soup.find('li','dw')
Nas = Nas.get_text().split() #['나스닥', '종합', '11.07.', '10,468.35', '전일대비', '하락', '6.90', '(-0.07%)']


print('   환영합니다. ' + nowdate + ', 세계 주식시장 지표입니다.')
print('   10초마다 갱신됩니다.')

while True:
    
    print('\n')
    print('코스피 : ', Kos[0])
    print('코스닥 : ', Kos[1])
    print('다우존스 : ', Dow[3], Dow[4]+Dow[5], Dow[6], Dow[7])
    print('나스닥 : ', Nas[2], Nas[3]+Nas[4], Nas[5], Nas[6])
    print('\n')
    print('\n')
    sleep(10)