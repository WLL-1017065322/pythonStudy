import time

al = "2019-5-10 23:40:00"

timeArray = time.strptime(al, "%Y-%m-%d %H:%M:%S")

timeStamp = int(time.mktime(timeArray))
print(timeStamp)

a2 = "2019/5/10 23:40:00"

timeArray = time.strptime(a2, "%Y-%m-%d %H:%M:%S")
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
print(otherStyleTime)
