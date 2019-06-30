
year = int(input("输入年份"))

def is_leapYear(year):
    if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
        print("{0}是闰年".format(year))
    else:
        print("{0}不是闰年".format(year))


is_leapYear(year)