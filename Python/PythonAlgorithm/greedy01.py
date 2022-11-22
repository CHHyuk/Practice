# 그리디 알고리즘
# 거스름돈 문제
"""
당신은 음식점의 계산을 도와주는 점원
카운터에는 거스름돈으로 사용할 500 100 50 10원 동전이 무한히 존재
손님에게 거슬러 주어야 할 돈이 N원일때 거슬러 주어야 할 동전의 최소 개수
N은 항상 10의 배수
"""
N = 1260
count = 0
    
# 큰 단위의 화폐부터 차례대로 확인
array = [500,100,50,10]
    
for coin in array:
    count += N // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 count
    N %= coin

print(count)