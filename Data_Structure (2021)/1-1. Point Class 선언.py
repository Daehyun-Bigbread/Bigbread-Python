# 1.
class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		
p = Point(1, 2)
print(p)

#실행결과: <__main__.Point object at 0x7f652e778438>


# 2.
class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def __str__(self):
		return f"({self.x}, {self.y})"
	
p = Point(1, 2)		# x = 1, y = 2인 객체 생성
print(p)			# p.__str__()이 호출되고, 리턴된 "(1, 2)"를 출력함

#실행결과: (1, 2)


# 3.
class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def __str__(self):
		return f"({self.x}, {self.y})"
	
p = Point(1, 2)
s = str(p)			# p.__str__() 형식으로 호출됨
print(s)			# s = "(1, 2)"

#실행결과: (1, 2)
