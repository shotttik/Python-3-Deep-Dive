# s = [1, 2, 3]
# print(len(s))
# from math import sqrt
# print(sqrt(4))
# import math
# print(math.pi)
# print(math.exp(1))
#
#
# def func_1():
# 	print('running func_1')
# func_1()
#
#
# def func_2(a: int, b: int):
# 	return a * b
#
# print(func_2(2,3))
# print(func_2('a', 3))
# print(func_2([1, 2], 3))
#
#
# def func_3():
# 	return func_4()
#
#
# def func_4():
# 	return 'running func_4'
#
# func_3()
#
# lambda
# lambda x: x**2
# fn1 = lambda x: x**2
# print(fn1)
# print(fn1(2))
#
# while loop
# i = 0
# while i < 5:
# 	print(i)
# 	i += 1
# i = 5
#
# while True:
# 	print(i)
# 	if i >= 5:
# 		break 
# 		print('something')
# min_length = 2
# name = input("please enter your name")
#
# while not(len(name) >= min_length and name.isprintable() and name.isalpha()):
# 	name = input("please enter your name")
#
# print(f'hello, {name}')
#
# min_length = 2
#
#
# while True:
# 	name = input("please enter your name")
# 	if (len(name) >= min_length and name.isprintable() and name.isalpha()):
# 		break
#
# print(f'hello, {name}')
#
# a = 0
#
# while a < 10:
# 	a += 1
# 	if a % 2 == 0:
# 		continue
# 	print(a)
#
# l = [1, 2, 3, 10]
# val = 10
#
# found = False
# idx = 0
# while idx < len(l):
# 	if l[idx] == val:
# 		found = True
# 		break
# 	idx += 1
#
# if not found:
# 	l.append(val)
# print(l)	
#
# l = [1, 2, 3]
# val = 10
# idx = 0
# while idx < len(l):
# 	if l[idx] == val:
# 		break
# 	idx +=1	
# else:
# 	l.append(val)	
#
# print(l)	
# '''Break, Continue and the Try Statement'''
# a = 10
# b = 1
# try:
# 	a/0
# except ZeroDivisionError:
# 	print('division by 0')
# finally:
# 	print("this always executes")
# a = 0
# b = 2
#
# while a < 4:
# 	print('------------------------')
# 	a += 1
# 	b -= 1
#
# 	try:
# 		a / b
# 	except ZeroDivisionError:
# 		print(f"{a}, {b} - division by 0")
# 		continue
# 	finally:
# 		print(f"{a}, {b} - always executes")
#
# 	print(f"{a}, {b} - main loop")	
# a = 0
# b = 2
#
# while a < 4:
# 	print('------------------------')
# 	a += 1
# 	b -= 10
#
# 	try:
# 		a / b
# 	except ZeroDivisionError:
# 		print(f"{a}, {b} - division by 0")
# 		break
# 	finally:
# 		print(f"{a}, {b} - always executes")

# 	print(f"{a}, {b} - main loop")
# else:
# 	print('code executed without a zero division error')
#
# '''The For Loop'''	
# '''In python, an iterable is an object capable of returning values one at a time'''		
# i = 0
# while i < 5:
# 	print(i)
# 	i +=1	
# i = None
# for i in range(5):
# 	print(i)
# for i in [1, 2, 3, 4]:
# 	print(i)
# for c in 'hello':
# 	print(c)
# for i,j in [(1,2), (2,3), (5,6)]:
# 	print(i, j)
#
# for i in range(5):
# 	if i==3:
# 		break
# 	print(i)	
#
# for i in range(1, 8):
# 	print(i)
# 	if i % 7 == 0:
# 		print('multiple of 7 found')
# 		break
# else:
# 	print('no multiples of 7 in the range')
# for i in range(5):
# 	print('-------------------------')
# 	try:
# 		10 / (i-3)
# 	except ZeroDivisionError:
# 		print("divided by 0")
# 		continue
# 	finally:
# 		print('always run')
#
# 	print(i)		
# s = 'hello'
# for c in s:
# 	print(c)
#
# s = 'hello'
# i = 0
# for c in s:
# 	print(i, c)
# 	i += 1
#	
# s = 'hello'
#
# for i in range(len(s)):
# 	print(i, s[i])
# s = 'hello'
#
# for i, c in enumerate(s):
# 	print(i, c)
#
# b = 'break'
# for i, c in enumerate(b):
# 	print(i, c)
#
# '''Clasess'''
# class Rectangle:
# 	def __init__(self, width, height):
# 		self.width = width
# 		self.height = height
# r1 = Rectangle(10, 20)		
# print(r1.width)
# r1.width = 100
# print(r1.width)
#
# class Rectangle:
# 	def __init__(self, width, height):
# 		self.width = width
# 		self.height = height
#
# 	def area(self):
# 		return self.width * self.height
#
# 	def perimeter(self):
# 		return 2 * (self.width + self.height)	
#
# r1 = Rectangle(10, 20)
# print(r1.area())
# print(r1.perimeter())
# print(hex(id(r1)))
#
# class Rectangle:
# 	def __init__(self, width, height):
# 		self.width = width
# 		self.height = height
#
# 	def area(self):
# 		return self.width * self.height
#
# 	def perimeter(self):
# 		return 2 * (self.width + self.height)	
#
# 	def __str__(self):
# 		return f'Rectangle: width={self.width}, height={self.height}'
#
# 	def __repr__(self):
# 		return f'Rectangle({self.width}, {self.height})'
#
# r1 = Rectangle(10, 20)
# print(str(r1))
# print(r1)
#
# r2 = Rectangle(10, 20)
# print(r1 is not r2)
# print(r1 == r2)
#
# class Rectangle:
# 	def __init__(self, width, height):
# 		self._width = width
# 		self._height = height
#
# 	def area(self):
# 		return self.width * self.height
#
# 	def perimeter(self):
# 		return 2 * (self.width + self.height)	
#
# 	def __str__(self):
# 		return f'Rectangle: width={self.width}, height={self.height}'
#
# 	def __repr__(self):
# 		return f'Rectangle({self.width}, {self.height})'
#
# 	def __eq__(self, other):
# 		if isinstance(other, Rectangle):
# 			return self.width == other.width and self.height == other.height
# 		else:
# 			return False
#
# 	def __lt__(self, other):
# 		if isinstance(other , Rectangle):
# 			return self.area() < other.area()
# 		else:
# 			return NotImplemented
#
# 	def get_width(self):
# 		return self._width		
#
# r1 = Rectangle(10, 20)		
# r2 = Rectangle(100, 200)
# print(r1 is not r2)
# print(r1 == r2)
# print(r2 > r1)
#
#
#
# class Rectangle:
# 	def __init__(self, width, height):
# 		self._width = width
# 		self._height = height
#	
# 	def get_width(self):
# 		return self._width
#
# 	def set_width(self, width):
# 		if width <= 0:
# 			raise ValueError("Width must be positive")
# 		else:
# 			self._width = width
#
# 	def get_height(self):
# 		return self._height
#
# 	def set_height(self, height):
# 		if height <= 0:
# 			raise ValueError("Height must be positive")			
# 		else:
# 			self._width = width
#
# 	def __str__(self):
# 		return f'Rectangle: width={self._width}, height={self._height}'
#
# 	def __repr__(self):
# 		return f'Rectangle({self._width}, {self._height})'
#
# 	def __eq__(self, other):
# 		if isinstance(other, Rectangle):
# 			return self._width == other._width and self._height == other._height
# 		else:
# 			return False
# class Rectangle:
# 	def __init__(self, width, height):
# 		self.width = width
# 		self.height = height
#
# 	@property
# 	def width(self):
# 		return self._width
#
# 	@width.setter
# 	def width(self, width):
# 		if width <= 0:
# 			raise ValueError("Width must be positive.")
# 		else:
# 			self._width = width
#
# 	@property
# 	def height(self):
# 		return self._height
#
# 	@height.setter
# 	def height(self, height):
# 		if height <= 0:
# 			raise ValueError("height must be positive.")
# 		else:
# 			self._height = height		
#	
#
# 	def __str__(self):
# 		return f'Rectangle: width={self.width}, height={self.height}'
#
# 	def __repr__(self):
# 		return f'Rectangle({self.width}, {self.height})'
#
# 	def __eq__(self, other):
# 		if isinstance(other, Rectangle):
# 			return self.width == other.width and self.height == other.height
# 		else:
# 			return False
#
# r1 = Rectangle(10, 20)
# print(r1.width)
# r1.width = 100
# print(r1)
# print(r1.height)
# r1 = Rectangle(-100, 20)
# print(r1)

class Cube:
	def __init__(self, height, width, length):
		self.height = height
		self.width = width
		self.length = length

	@property
	def width(self):
		return self._width
	
	@width.setter
	def width(self, width):
		if width <= 0:
			raise ValueError("Width must be positive")
		else:
			self._width = width

	@property
	def height(self):
		return self._height
	
	@height.setter
	def height(self, height):
		if height <= 0:
			raise ValueError("Height must be positive")
		else:
			self._height = height
	
	@property
	def length(self):
		return self._length

	@length.setter
	def length(self, length):
		if length <= 0:
			raise ValueError("Length must be positive")
		else:
			self._length = length
		

	def __repr__(self):
		return f'Cube({self.height}, {self.width}, {self.length})'

	def __str__(self):
		return 'Cube STR'	
	

c1 = Cube(2, 5, 8)
print(c1)
c1.width = -5
