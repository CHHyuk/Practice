import requests 

url = "https://www.google.com/search?q=%EC%BD%94%EC%9D%B8+%EA%B0%80%EA%B2%A9&sxsrf=ALiCzsaFFp-_vlBbYWRijeX9DoxhOXxeeA%3A1667842561709&ei=AUJpY5z6Ksum-QbO4Lb4Bg&ved=0ahUKEwjc_rnbzZz7AhVLU94KHU6wDW8Q4dUDCA8&uact=5&oq=%EC%BD%94%EC%9D%B8+%EA%B0%80%EA%B2%A9&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQsQMQgwEQQzIFCAAQgAQyBAgAEEMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgsIABCABBCxAxCDAToRCC4QgAQQsQMQgwEQxwEQ0QM6CwguEIAEEMcBENEDOggIABCABBCxAzoQCC4QsQMQgwEQxwEQ0QMQQ0oECEEYAEoECEYYAFAAWIYKYIQLaAJwAHgBgAGZAYgBiAuSAQQwLjEwmAEAoAEBwAEB&sclient=gws-wiz-serp" 
response = requests.get(url) 
print(response.status_code) # 200 = 추출가능
print(response.text) # 해당 사이트의 html 전부 출력