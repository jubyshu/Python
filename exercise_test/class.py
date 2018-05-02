class Student(object):
	
	def __init__(self, name, gender):
		self.name = name
		self.__gender = gender

	def get_gender(self):
		return self.__gender

	def set_gender(self, gender):
		if gender == 'male' or 'female':
			self.__gender = gender
		else:
			raise ValueError('wrong gender')

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


# 为了统计学生人数，
# 可以给Student类增加一个类属性，
# 每创建一个实例，
# 该属性自动增加
class  Student(object):
	count = 0

	def __init__(self, name):
		self.name = name
		Student.count += 1

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
