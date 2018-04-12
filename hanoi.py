
def move(n, a, b, c):
	if n == 1:
		print(a, '-->', c)
	else:
		#将n-1个盘子从A移到B
		move(n-1, a, c, b)
		#将1个盘子从A移到C
		move(1, a, b, c)
		#将n-1个盘子从B移到C
		move(n-1, b, a, c)
	return
print(move(3, 'A', 'B', 'C'))