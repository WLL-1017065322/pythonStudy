##公式 ：  (s*(s-a)*(s-b)*(s-c)) ** 0.5

a = float(input('输入a:'))
b = float(input('输入b:'))
c = float(input('输入c:'))

s = (a+b+c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print('面积：%0.2f' %area)