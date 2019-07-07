

import calendar

def minth_Range(yy,mm):
    monthRange = calendar.monthrange(yy,mm)
    print(monthRange)

minth_Range(2019,7)