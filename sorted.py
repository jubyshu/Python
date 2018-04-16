#按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]

L2 = sorted(L, key=by_name)
print(L2)

#按成绩从高到低排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_score(t):
	return -t[1]

L2 = sorted(L, key=by_score)
print(L2)


#闭包
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

#返回递增整数
def createCounter():
	s = [0]
	def counter():
		s[0] += 1
		return s[0]
	return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

#匿名函数
L = list(filter(lambda n: n%2==1, range(1, 20)))
print(L)