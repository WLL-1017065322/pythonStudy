# num = float(input('输入数字:'))
#
# num_sqrt = num ** 0.5
#
# print('%.3f的平方根为%.3f'%(num,num_sqrt))

##以上只适用于正数

import cmath

a = int(input('输入a:'))

a_sqrt = cmath.sqrt(a)

print('{0}的平方根是：{1:0.3f}+{2:0.3f}'.format(a,a_sqrt.real,a_sqrt.imag))