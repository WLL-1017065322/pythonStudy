
import datetime

def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days = 2)
    yesterday = today - oneday
    print(oneday)
    return yesterday
print(getYesterday())