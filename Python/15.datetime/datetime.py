import datetime

print(datetime.datetime.now())

start_time = datetime.datetime.now()
print(type(start_time))

start_time.replace(year = 2017, month = 2 , day = 2)
print(start_time)
start_time = start_time.replace(year = 2017, month = 2 , day = 2)
print(start_time)

start_time = datetime.datetime(2022,2,2)
print(start_time)

how_long = start_time - datetime.datetime.now()
print(type(how_long))

print(how_long.days)
print(how_long.seconds)
print("2월 1일까지는 {}일 {}시간이 남았습니다.".format(how_long.days, how_long.seconds//3600))
