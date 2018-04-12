import math

def quadratic(a, b, c):
	if not isinstance(a|b|c, (int, float)):
		raise TypeError('bad operand type')

	delta=b*b-4*a*c
	if delta==0:
		#print('only one solution')
		x=b/(-2*a)
		return x
	elif delta<0:
		#print('no solution')
		return
	else:
		#print('two solution')
		x1=(-b+math.sqrt(delta))/(2*a)
		x2=(-b-math.sqrt(delta))/(2*a)
		return x1, x2

print('quadratic(2, 3, 1)=', quadratic(2, 3, 1))
print('quadratic(1, 3, -4)=', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
	print('测试失败')
elif quadratic(1, 3, -4)!= (1.0, -4.0):
	print('测试失败')
else:
	print('测试成功')