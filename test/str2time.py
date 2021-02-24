import time

a1 = "2019-5-10 23:40:00"
# 先转换为时间数组
timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")

# 转换为时间戳
timeStamp = int(time.mktime(timeArray))
print(timeStamp)

a1 = "2019-5-10 23:40"
# 先转换为时间数组
timeArray = time.strptime(a1, "%Y-%m-%d %H:%M")

# 转换为时间戳
timeStamp = int(time.mktime(timeArray))
print(timeStamp)
