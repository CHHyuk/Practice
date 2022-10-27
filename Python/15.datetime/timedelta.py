import datetime

hundred = datetime.timedelta(days = 100)
print(datetime.datetime.now() + hundred)

hundred_before = datetime.timedelta(days = -100)
print(datetime.datetime.now() + hundred_before)
print(datetime.datetime.now() - hundred)

tomorrow = datetime.datetime.now().replace(hour = 9, minute = 0, second = 0) + datetime.timedelta(days = 1)
print(tomorrow)