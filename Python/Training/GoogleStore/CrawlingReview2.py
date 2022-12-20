from google_play_scraper import Sort, reviews_all

result = reviews_all(
    'com.dobrain.verified',
    sleep_milliseconds=1000,
    lang='ko', 
    country='kr', 
    sort=Sort.MOST_RELEVANT, 
    filter_score_with=None 
)

review = []
for i in range(len(result)):
    temp = [result[i].get('userName'),result[i].get('score'),result[i].get('content')]
    review.append(temp)

print(*review, sep='\n')