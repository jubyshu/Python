#字符串转为浮点数
from functools import reduce

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
	def fl(x,y):
		return x * 10 + y
	def char2num(s):
		return digits[s]

	str1, str2 = s.split('.')
	f1 = reduce(fl, map(char2num, str1))
	f2 = reduce(fl, map(char2num, str2))
	return f1 + f2 * .1 ** len(str2)
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
