#
#'''Single Inheritance'''
#
# class Shape:
# 	pass

# class Ellipse(Shape):
# 	pass

# class Circle(Ellipse):
# 	pass

# class Polygon(Shape):
# 	pass

# class Rectangle(Polygon):
# 	pass

# class Square(Rectangle):
# 	pass

# class Triangle(Polygon):
# 	pass

# print(issubclass(Ellipse, Shape))
# print(issubclass(Circle, Shape))
# print(issubclass(Polygon, Ellipse))
# print(issubclass(Square, Shape))

# s = Shape()
# e = Circle()
# sq = Square()
# print(isinstance(s, Shape))
# print(isinstance(e, Shape))
# print(isinstance(e, Ellipse))

# print(type(Shape))
# print(type(s))

# sq = Square()
# p = Polygon()
# print(sq, p)

# class Person:
# 	pass

# print(issubclass(Person, object))

#
#'''The object class'''
#
# class Person:
# 	pass
# print(issubclass(Person, object))
# print(issubclass(int, object))
# import math
# print(type(math))
# import types
# print(dir(types))

# def my_func():
# 	pass
# print(type(my_func))

# print(types.FunctionType is type(my_func))

# class Person:
# 	pass

# p= Person()

# print(str(p), repr(p))
# o1 = object()
# o2 = object()
# print(id(o1), id(o2))
# print(o1 is o2)
# print(o1 == o2)
#
#'''Overriding'''
#
# class Person:
# 	pass
# p = Person()
# print(str(p))

# class Person:
# 	def __str__(self):
# 		return 'Person Class'
# p = Person()
# print(str(p))

# class Person:
# 	def __repr__(self):
# 		return 'Person() with extra debugging info'

# p = Person()
# print(str(p))
# print(p.__str__())

# class Shape:
# 	def __init__(self, name):
# 		self.name = name

# 	def info(self):
# 		return f'Shape.info called for Shape({self.name})'

# 	def extended_info(self):
# 		return f'Shape.extended_info called for Shape({self.name})'

# class Polygon(Shape):
# 	def __init__(self, name):
# 		self.name = name

# 	def info(self):
# 		return f'Polygon info called for Polygon({self.name})'
# p = Polygon('Square')
# print(p.info())
# print(p.extended_info())

# class Shape:
# 	def __init__(self, name):
# 		self.name = name

# 	def info(self):
# 		return f'Shape.info called for Shape({self.name})'

# 	def extended_info(self):
# 		return f'Shape.extended_info called for Shape({self.name})', self.info()

# class Polygon(Shape):
# 	def __init__(self, name):
# 		self.name = name

# 	def info(self):
# 		return f'Polygon info called for Polygon({self.name})'
# p = Polygon('Square')
# print(p.info())
# print(p.extended_info())
#
# class Person:
# 	def __str__(self):
# 		return 'Person.__str__ called'

# class Student(Person):
# 	def __repr__(self):
# 		return 'Student.__repr__ called'

# s = Student()
# print(str(s))
#
# class Person:
# 	def __str__(self):
# 		print('Person.__str__ called')
# 		return self.__repr__()

# 	def __repr__(self):
# 		return str(hex(id(self)))

# class Student(Person):
# 	def __repr__(self):
# 		return 'Student.__repr__ called'

# s = Student()
# print(str(s))
# print(repr(s))

# p = Person()
# print(str(p))
#
#'''Extending'''
#
# class Person:
# 	pass

# class Student(Person):
# 	def study(self):
# 		return 'study....' * 3

# p = Person()
# # print(p.study())
# s = Student()
# print(s.study())
# class Person:
# 	def rountine(self):
# 		return self.eat() + self.study() + self.sleep()

# 	def eat(self):
# 		return 'Person eats...'

# 	def sleep(self):
# 		return 'Person sleeps...'

# p = Person()
# #p.rountine()
# class Student(Person):
# 	def study(self):
# 		return 'student study....'
# s = Student()
# print(s.rountine())

# class Person:
# 	def rountine(self):
# 		result = self.eat()
# 		if hasattr(self, 'study'):
# 			result += self.study()
# 		result += self.sleep()
# 		return result

# 	def eat(self):
# 		return 'Person eats...'

# 	def sleep(self):
# 		return 'Person sleeps...'

# p = Person()
# print(p.rountine())
# class Student(Person):
# 	def study(self):
# 		return 'student study....'
# s = Student()
# print(s.rountine())

# class Account:
# 	apr = 3.0

# 	def __init__(self, account_number, balance):
# 		self.account_number = account_number
# 		self.balance = balance
# 		self.account_type = 'Generic Account'

# 	def calc_interest(self):
# 		return f'Calculating interest on { .account_type} with APR = {self.apr}'

# a = Account(123, 100)
# print(a.apr, a.account_type, a.calc_interest())

# class Savings(Account):
# 	apr = 5.0

# 	def __init__(self, account_number, balance):
# 		self.account_number = account_number
# 		self.balance = balance
# 		self.account_type = 'Savings Account'
# s = Savings(234, 200)
# print(s.apr, s.account_type, s.calc_interest())
# print(Account.apr, Savings.apr)
#
#'''Delegating to parent'''
#
# class Person:
# 	def work(self):
# 		return 'Person works...'


# class Student(Person):
# 	def work(self):
# 		result = super().work()
# 		return f'Student works... and {result}'

# s = Student()
# print(s.work())

# class Person:
# 	def work(self):
# 		return 'Person works...'

# class Student(Person):
# 	pass

# class PythonStudent(Student):
# 	def work(self):
# 		result = super().work()
# 		return f'PythonStudent codes... and {result}'
# ps = PythonStudent()
# print(ps.work())


# class Person:
# 	def work(self):
# 		return 'Person works...'

# class Student(Person):
# 	def work(self):
# 		result = super().work()
# 		return f'Student studies... and {result}'

# class PythonStudent(Student):
# 	def work(self):
# 		result = super().work()
# 		return f'PythonStudent codes... and {result}'
# ps = PythonStudent()
# print(ps.work())
#

# class Person:
# 	def work(self):
# 		return 'Person works...'

# class Student(Person):
# 	def study(self):
# 		return 'student studies...'

# class PythonStudent(Student):
# 	def code(self):
# 		result_1 = self.work()
# 		result_2 = self.study()
# 		return f'{result_1} and {result_2} and PythonStudent codes..'

# ps = PythonStudent()
# print(ps.code())


# class Person:
# 	def work(self):
# 		return f'{self} works...'

# class Student(Person):
# 	def work(self):
# 		result = super().work()
# 		return f'{self} studies... and {result}'

# class PythonStudent(Student):
# 	def work(self):
# 		result = super().work()
# 		return f'{self} codes... and {result}'

# ps = PythonStudent()
# print(hex(id(ps)))
# print(ps.work())

# class Person:
# 	def set_name(self, value):
# 		print('setting name using Person set_name method...')
# 		self.name= value

# class Student(Person):
# 	def set_name(self, value):
# 		print('Student class is delegating back to parent...')
# 		super().set_name(value)

# s = Student()
# s.set_name('Alex')
# print(s.__dict__)

# class Person:
# 	def __init__(self, name):
# 		self.name = name

# class Student(Person):
# 	def __init__(self, name, student_number):
# 		super().__init__(name)
# 		self.student_number = student_number
# s = Student('Python', 30)
# print(s.__dict__)

# class Person:
# 	def __init__(self, name):
# 		self.name = name

# class Student(Person):
# 	pass

# s = Student('Mark')
# print(s.__dict__)

# from math import pi
# from numbers import Real 

# class Circle:
# 	def __init__(self, r):
# 		self._r = r
# 		self._area = None
# 		self._perimeter = None

# 	@property
# 	def radius(self):
# 		return self._r

# 	@radius.setter
# 	def radius(self, r):
# 		if isinstance(r, Real) and r > 0:
# 			self._r = r
# 			self._area = None
# 			self._perimeter = None
# 		else:
# 			raise ValueError('Radius must be a positive real number.')
	
# 	@property
# 	def area(self):
# 		if self._area is None:
# 			self._area = pi * self.radius ** 2
# 		return self._area
	
# 	@property
# 	def perimeter(self):
# 		if self._perimeter is None:
# 			self._perimeter = 2 * pi * self.radius
# 		return self._perimeter

# class UnitCircle(Circle):
# 	def __init__(self):
# 		super().__init__(1)

# u = UnitCircle()
# print(u.radius, u.area, u.perimeter)

# u.radius = 10
# print(u.radius, u.area, u.perimeter)

# class UnitCircle(Circle):
# 	def __init__(self):
# 		super().__init__(1)

# 	@property
# 	def radius(self):
# 		return super().radius
	
# u = UnitCircle()
# print(u.radius, u.area, u.perimeter)

# ##u.radius = 10 AttributeError: can't set attribute ERROR!
# print(u.radius, u.area, u.perimeter)


# from math import pi
# from numbers import Real 

# class Circle:
# 	def __init__(self, r):
# 		self._set_radius(r)
# 		self._area = None
# 		self._perimeter = None

# 	@property
# 	def radius(self):
# 		return self._r

# 	def _set_radius(self, r):
# 		if isinstance(r, Real) and r > 0:
# 			self._r = r
# 			self._area = None
# 			self._perimeter = None
# 		else:
# 			raise ValueError('Radius must be a positive real number.')

# 	@radius.setter
# 	def radius(self, r):
# 		self._set_radius(r)

# 	@property
# 	def area(self):
# 		if self._area is None:
# 			self._area = pi * self.radius ** 2
# 		return self._area
	
# 	@property
# 	def perimeter(self):
# 		if self._perimeter is None:
# 			self._perimeter = 2 * pi * self.radius
# 		return self._perimeter


# class UnitCircle(Circle):
# 	def __init__(self):
# 		super().__init__(1)

# 	@property
# 	def radius(self):
# 		return super().radius
	
# u = UnitCircle()
# print(u.radius, u.area, u.perimeter)

### u.set_radius(10)
# print(u.radius, u.area, u.perimeter)

#'''Slots'''

# class Location:
# 	__slots__ = 'name', '_longitude', '_latitude'

# 	def __init__(self, name, longitude, latitude):
# 		self.name = name
# 		self._longitude = longitude
# 		self._latitude = latitude

# 	@property
# 	def longitude(self):
# 		return self._longitude
	
# 	@property
# 	def latitude(self):
# 		return self._latitude

# print(Location.__dict__)
# Location.map_service = 'Google Maps'
# print(Location.__dict__)

# l = Location('Mumbai', longitude=19.0760, latitude=72.8777)
# print(l.name, l.longitude, l.latitude)
# ##print(l.__dict__)
# ##l.map_link = 'https://????...'

#'''Slots and single inheritance'''

# class Person:
# 	def __init__(self, name):
# 		self.name = name

# class Student(Person):
# 	pass

# s = Student('Alex')
# print(s.__dict__)

# class Person:
# 	__slots__ = 'name',

# 	def __init__(self, name):
# 		self.name = name

# class Student(Person):
# 	pass

# P = Person('Alex')
# ##print(p.__dict__)
# s = Student('Alex')
# print(s.__dict__)
# s.age = 30
# print(s.age)

class Person:
	__slots__ = 'name',

	def __init__(self, name):
		self.name = name

class Student(Person):
	__slots__ = 'school', 'student_number'

	def __init__(self, name, school, student_number):
		super().__init__(name)
		self.school = school
		self.student_number = student_number

s = Student('James Pont', ' MI6 Prep', '008')
print(s.name, s.school, s.student_number)
##print(s.__dict__)