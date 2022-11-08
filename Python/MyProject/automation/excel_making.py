# 새 엑셀 파일 생성
import openpyxl

wb = openpyxl.Workbook() # 새 워크북 생성
ws = wb.active #현재 활성화된 sheet 가져옴, ws = wb['sheet']
ws.title = '카페 메뉴' # 시트 이름
ws.append(['넘버','카페이름','메뉴'])


for i in range(1,31):
    if i <= 10:
        cafe_name = '스타벅스'
        if i % 3 == 0:
            menu = '아메리카노'
        elif i % 2 == 0:
            menu = '녹차'
        else:
            menu = '카페라떼'
    elif i <= 20:
        cafe_name = '파스쿠치'
        if i % 3 == 0:
            menu = '아메리카노'
        elif i % 2 == 0:
            menu = '녹차'
        else:
            menu = '카페라떼'
    elif i <= 30:
        cafe_name = '투썸플레이스'
        if i % 3 == 0:
            menu = '아메리카노'
        elif i % 2 == 0:
            menu = '녹차'
        else:
            menu = '카페라떼'
    ws.append([i,cafe_name,menu])


wb.save('C:/git/practice/python/MyProject/automation/excel_cafe.xlsx') # 경로에 저장
wb.close()