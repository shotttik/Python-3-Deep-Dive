#'''Polymorphism and Special Methods'''
#
#'''__str__ and __repr__'''
#
# class Person:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# 	def __repr__(self):
# 		print('__repr__ called')
# 		return f'Person (name="{self.name}", age={self.age})'
#
# 	def __str__(self):
# 		print('__str__ called')
# 		return self.name
#
# p = Person('Python', 30)
# p
# print(p)
# print(str(p))
#
# class Person:
# 	pass
#
# class Point:
# 	pass
#
# person = Person()
# point = Point()
# print(repr(person), '|', repr(point))
# print(str(person), '|', str(point))
#
# class Person:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# 	def __str__(self):
# 		print('__str__ called')
# 		return self.name
#
# p = Person('Python', 30)
# print(repr(p))
# print(p)
#
#
# class Person:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# 	def __repr__(self):
# 		print('__repr__ called')
# 		return f'Person (name="{self.name}", age={self.age})'
#
# 	def __str__(self):
# 		print('__str__ called')
# 		return self.name
#
#
# p = Person('Python', 30)
# print(f'the person is {p}')
# 'the person is {}'.format(p)
# 'the person is %s' % p
#
#'''Arithmetic Operators'''
#
# from numbers import Real
# from math import sqrt
#
# class VectorDimensionMismatch(TypeError):
# 	pass
#
# class Vector:
# 	def __init__(self, *components):
# 		if len(components) < 1:
# 			raise ValueError('Cannot create an empty vector.')
# 		for component in components:
# 			if not isinstance(component, Real):
# 				raise ValueError(f'Vector componentes must all be real numbers. {component} is invalid')
# 		self._components = tuple(components)
#
# 	def __len__(self):
# 		return len(self._components)
#
# 	@property
# 	def components(self):
# 		return self._components
#	
# 	def __repr__(self):
# 		return f'Vector {self.components}'
#
# 	def validate_type_and_dimension(self, v):
# 		return isinstance(v, Vector) and len(v) == len(self)
#
# 	def __add__(self, other):
# 		if not self.validate_type_and_dimension(other):
# 			return NotImplemented
# 		components = (x + y for x, y in zip(self.components, other.components))
# 		return Vector(*components)
#
# 	def __sub__(self, other):
# 		if not self.validate_type_and_dimension(other):
# 			return NotImplemented
# 		components = (x - y for x, y in zip(self.components, other.components))
# 		return Vector(*components)
#
# 	def __mul__(self, other):
# 		print('__mul__ called...')
# 		if isinstance(other, Real):
# 			# scalar product
# 			components = (other * x for x in self.components)
# 			return Vector(*components)
# 		if self.validate_type_and_dimension(other):
# 			# dot product
# 			components = (x * y for x, y in zip(self.components, other.components))
# 			return sum(components)
# 		return NotImplemented
#
# 	def __rmul__(self, other):
# 		return self * other
#
# 	def __iadd__(self, other):
# 		print('_iadd__ called...')
# 		if self.validate_type_and_dimension(other):
# 			components = (x + y for x, y in zip(self.components, other.components))
# 			self._components = tuple(components)
# 			return self
# 		return self + other
#
# 	def __neg__(self):
# 		print('__neg__ called...')
# 		components = (-x for x in self.components)
# 		return Vector(*components)
#
# 	def __abs__(self):
# 		print('__abs__ called...')
# 		return sqrt(sum(x **2 for x in self.components))
#
# v1 = Vector(1,1)
# print(abs(v1))
#
# v1 = Vector(1, 2)
# print(id(v1))
# v2 = -v1
# print(id(v2))
# print(v2)
# v1 = Vector(1, 2)
# v2 = Vector(10, 10)
# print(id(v1))
# v1 += v2
# print(id(v1), v1)
#
# # '''In-Place Operators'''
# l = [1, 2]
# print(id(l))
# l += [3,4]
# print(id(l), l)
#
# l = [1, 2]
# print(id(l))
# l = l + [3, 4]
# print(id(l), l)
#
#
# class Person:
# 	def __init__(self, name):
# 		self.name = name
#
# 	def __repr__(self):
# 		return f"Person ('{self.name}')"
# p1 = Person('John')
# print(p1)
#
# class Family:
# 	def __init__(self, mother, father):
# 		self.mother = mother
# 		self.father = father
# 		self.children = []
#
# 	def __iadd__(self, other):
# 		self.children.append(other)
# 		return self
# f = Family(Person('Mary'), Person('John'))
# print(f.mother, f.father, f.children)
# f += Person('Beqa')
# print(f.children)
# f += Person('Michael')
# print(f.children)
#
#'''Rich Comprasions'''
#
# class Vector:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
#
# 	def __repr__(self):
# 		return f'Vector(x={self.x}, y={self.u})'
#
# v1 = Vector(0, 0)
# v2 = Vector(0, 0)
# print(id(v1), id(v2))
# print(v1 == v2, v1 is v2)
#
# class Vector:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
#
# 	def __repr__(self):
# 		return f'Vector(x={self.x}, y={self.u})'
#
# 	def __eq__(self, other):
# 		if isinstance(other, Vector):
# 			return self.x == other.x and self.y == other.y
# 		return NotImplemented
#
# v1 = Vector(1, 1)
# v2 = Vector(1, 1)
# v3 = Vector(10, 10)
# print(v1 == v2, v1 is v2)
# print(v1 == v3)
#
# class Vector:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
#
# 	def __repr__(self):
# 		return f'Vector(x={self.x}, y={self.u})'
#
# 	def __eq__(self, other):
# 		print('__eq__ called...')
# 		if isinstance(other, tuple):
# 			other = Vector(*other)
# 		if isinstance(other, Vector):
# 			return self.x == other.x and self.y == other.y
# 		return NotImplemented
#
# v1 = Vector(10, 11)
# print(v1 == (10, 11))
# print((10, 11) == v1)
# from math import sqrt
# class Vector:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
#
# 	def __repr__(self):
# 		return f'Vector(x={self.x}, y={self.u})'
#
# 	def __eq__(self, other):
# 		print('__eq__ called...')
# 		if isinstance(other, tuple):
# 			other = Vector(*other)
# 		if isinstance(other, Vector):
# 			return self.x == other.x and self.y == other.y
# 		return NotImplemented
#
# 	def __abs__(self):
# 		return sqrt(self.x **2 + self.y **2)
#
# 	def __lt__(self, other):
# 		print('__lt__ called...')
# 		if isinstance(other, tuple):
# 			other = Vector(*other)
# 		if isinstance(other, Vector):
# 			return abs(self) < abs(other)
#
# v1 = Vector(0, 0)
# v2 = Vector(1, 1)
#
# print(v1 < v2)
# print(v2 > v1)
# print(v1 < (1, 1))
# print((1,1) > v1)
#
# from math import sqrt
# class Vector:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
#
# 	def __repr__(self):
# 		return f'Vector(x={self.x}, y={self.u})'
#
# 	def __eq__(self, other):
# 		print('__eq__ called...')
# 		if isinstance(other, tuple):
# 			other = Vector(*other)
# 		if isinstance(other, Vector):
# 			return self.x == other.x and self.y == other.y
# 		return NotImplemented
#
# 	def __abs__(self):
# 		return sqrt(self.x **2 + self.y **2)
#
# 	def __lt__(self, other):
# 		print('__lt__ called...')
# 		if isinstance(other, tuple):
# 			other = Vector(*other)
# 		if isinstance(other, Vector):
# 			return abs(self) < abs(other)
#
# 	def __le__(self, other):
# 		print('__le__ called...')
# 		return self == other or self < other
#
# v1 = Vector(0, 0)
# v2 = Vector(0, 0)
# v3 = Vector(1, 1)
# print(v1 <= v2)
# print(v1 <= v3)
# print(v1 >= v3)
# print(v1 != v2)
# print(not(v1 == v2))
#
# from functools import total_ordering
#
# @total_ordering
# class Number:
# 	def __init__(self, x):
# 		self.x = x
#
# 	def __eq__(self, other):
# 		print('__eq__ called...')
# 		if isinstance(toher, Number):
# 			return self.x == other.x
# 		return NotImplemented
#
# 	def __lt__(self, other):
# 		print('__lt__ called...')
# 		if isinstance(other, Number):
# 			return self.x < other.x
# 		return NotImplemented
# a = Number(1)
# b = Number(2)
# c = Number(1)
# a < b
#
#'''Hashing and Equality'''
#
# class Person:
# 	pass
# p1 = Person()
# p2 = Person()
# print(hash(p1), hash(p2))
#
# class Person:
# 	def __init__(self, name):
# 		self.name = name
#
# 	def __eq__(self, other):
# 		return isinstance(other, Person) and self.name == other.name
#
# 	def __repr__(self):
# 		return f"Person name(name='{self.name}')"
#
# p1 = Person('John')
# p2 = Person('John')
# p3 = Person('Eric')
# print(p1 == p2)
# print(p1 == p3)
# ##print(hash(p1)) unhashable type. based on id
# print(type(p1.__hash__))
# print(p1.__hash__)
#
# class Person:
# 	def __init__(self, name):
# 		self._name = name
#
# 	@property
# 	def name(self): 
# 		return self._name
#
# 	def __eq__(self, other):
# 		return isinstance(other, Person) and self.name == other.name
#
# 	def __hash__(self):
# 		return hash(self.name)
#
# 	def __repr__(self):
# 		return f"Person name(name='{self.name}')"
#
# p1 = Person('Eric')
# print(hash(p1))
# p2 = Person('Eric')
# print(p1 == p2)
# print(hash(p1), hash(p2))
# d = {p1: 'Eric idle'}
# print(d)
#
#'''Booleans'''
#
# class Person:
# 	pass

# p = Person()
# print(bool(p))

# class MyList:
# 	def __init__(self, length):
# 		self._length = length

# 	def __len__(self):
# 		print('__len__ called...')
# 		return self._length
# l1 = MyList(0)
# l2 = MyList(10)
# print(bool(l1))
# print(bool(l2))
#
# class MyList:
# 	def __init__(self, length):
# 		self._length = length
#
# 	def __len__(self):
# 		print('__len__ called...')
# 		return self._length
#
# 	def __bool__(self):
# 		print('__bool__ called...')
# 		return self._length >0
#
# l1 = MyList(0)
# l2 = MyList(10)
# print(bool(l1))
# print(bool(l2))
#
# class Point:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
# p1 = Point(0, 0)
# p2 = Point(1, 1)
# print(bool(p1), bool(p2))
# class Point:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
#
# 	def __bool__(self):
# 		return self.x != 0 or self.y != 0
#
# p1 = Point(0, 0)
# p2 = Point(1, 1)
# print(bool(p1), bool(p2))
# print(bool(p1.x or p1.y))
# print(bool(p2.x or p2.y))
#
#
# print('--------------\nReturn int instead of boolean\n-----------')
# class Point:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
#
# 	def __bool__(self):
# 		return self.x or self.y
#
# p1 = Point(0, 0)
# p2 = Point(1, 1)
# # print(bool(p1), bool(p2)) __bool__ should return boolean !
# print(bool(p1.x or p1.y))
# print(bool(p2.x or p2.y))
#
# print('------------\nSolution\n----------')
#
# class Point:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
#
# 	def __bool__(self):
# 		return bool(self.x or self.y)
#
# p1 = Point(0, 0)
# p2 = Point(1, 1)
# print(bool(p1), bool(p2))
# print(bool(p1.x or p1.y))
# print(bool(p2.x or p2.y))
#
# '''Callables'''
#
# class Person:
# 	def __call__(self):
# 		print('__call__ called...')
# p = Person()
# p()
# print(type(p))
#
# from functools import partial
# print(type(partial))
#
# def my_func(a, b, c):
# 	return a, b, c
# print(type(my_func))
# #
# partial_func = partial(my_func, 10, 20)
# print(type(partial_func))
# print(partial_func(30))
#
# class Partial:
# 	def __init__(self, func, *args):
# 		self._func = func
# 		self._args = args
#
# 	def __call__(self, *args):
# 		return self._func(*self._args, *args)
# partial_func = Partial(my_func, 10, 20)
# print(type(partial_func))
# print(partial_func(30))
# print(callable(print))
# print(type(print))
#
# from collections import defaultdict
#
# def default_value():
# 	return 'n/a'
# d = defaultdict(default_value)
# print(d['A'])
#
from collections import defaultdict
# miss_counter = 0
# def default_value():
# 	global miss_counter
# 	miss_counter += 1
# 	return 'N/A'
# d = defaultdict(default_value)
# d['a'] = 1
# print(d['a'])
# print(miss_counter)
# print(d['b'])
# print(miss_counter)
#
# class DefaultValue:
# 	def __init__(self):
# 		self.counter = 0
# 
# 	def __iadd__(self, other):
# 		if isinstance(other, int):
# 			self.counter += other
# 			return self
# 		raise ValueError('Can only increment with an integer value')
# default_value_1 = DefaultValue()
# print(default_value_1.counter)
# default_value_1 += 1
# print(default_value_1.counter)
#
# class DefaultValue:
# 	def __init__(self):
# 		self.counter = 0
#
# 	def __iadd__(self, other):
# 		if isinstance(other, int):
# 			self.counter += other
# 			return self
# 		raise ValueError('Can only increment with an integer value')
#
# 	def __call__(self):
# 		self.counter += 1
# 		return 'N/A'
#
# def_1 = DefaultValue()
# def_2 = DefaultValue()
# cache_1 = defaultdict(def_1)
# cache_2 = defaultdict(def_2)
# print(def_1.counter)
# cache_1['a']
# cache_1['d']
# print(def_1.counter)
# print(def_2.counter)
# cache_2['a']
# print(def_2.counter)
# class DefaultValue:
# 	def __init__(self, default_value):
# 		self.default_value = default_value
# 		self.counter = 0
#
# 	def __call__(self):
# 		self.counter += 1
# 		return self.default_value
#
# cache_def_1 = DefaultValue(None)
# cache_def_2 = DefaultValue(0)
# cache_1 = defaultdict(cache_def_1)
# cache_2 = defaultdict(cache_def_2)
# print(cache_1['a'], cache_1['b'])
# print(cache_def_1.counter)
# print(cache_2['a'])
# print(cache_def_2.counter)
# from time import perf_counter
# from functools import wraps
#
# def profiler(fn):
# 	counter = 0
# 	total_elapsed = 0
# 	avg_time = 0
#
# 	@wraps(fn)
# 	def inner(*args, **kwargs):
# 		nonlocal counter
# 		nonlocal total_elapsed
# 		nonlocal avg_time
# 		counter += 1
# 		start = perf_counter()
# 		result = fn(*args, **kwargs)
# 		end = perf_counter()
# 		total_elapsed += (end - start)
# 		avg_time = total_elapsed / counter
# 		return result
#
# 	inner.counter = counter
# 	inner.avg_time = avg_time
# 	return inner
# from time import sleep
# import random
#
# random.seed(0)
#
# @profiler
# def func1():
# 	sleep(random.random())
#
# func1(), func1()
#
# print(func1.counter, func1.avg_time)
#
#
# from time import perf_counter
# from functools import wraps
# from time import sleep
# import random
#
# def profiler(fn):
# 	_counter = 0
# 	_total_elapsed = 0
# 	_avg_time = 0
#
# 	@wraps(fn)
# 	def inner(*args, **kwargs):
# 		nonlocal _counter
# 		nonlocal _total_elapsed
# 		nonlocal _avg_time
# 		_counter += 1
# 		start = perf_counter()
# 		result = fn(*args, **kwargs)
# 		end = perf_counter()
# 		_total_elapsed += (end - start)
# 		_avg_time = _total_elapsed / _counter
# 		return result
#
# 	def counter():
# 		return _counter
#
# 	def avg_time():
# 		return _avg_time
#
# 	inner.counter = counter
# 	inner.avg_time = avg_time
# 	return inner
#
# @profiler
# def func1():
# 	sleep(random.random())
# func1(), func1()
# func1.counter()
#
#'''The `__del__` method'''
# 
# import ctypes
#
# def ref_count(address):
# 	return ctypes.c_long.from_address(address).value
#
# class Person:
# 	def __init__(self, name):
# 		self.name = name
#
# 	def __repr__(self):
# 		return f'Person({self.name})'
#
# 	def __del__(self):
# 		print(f'__del__ called for {self}...')
#
# 	def gen_ex(self):
# 		raise ValueError('Something went bump')
#
# p = Person('Alex')
# id_p = id(p)
# print(ref_count(id_p))
# try:
# 	p.gen_ex()
# except ValueError as ex:
# 	error = ex
# 	print(ex)
#
#''' The __format__ method
#
# a = 0.1
# from datetime import datetime
# print(format(a, '.20f'))
# now = datetime.utcnow()
# now
# print(format(now, '%a %Y-%m-%d %I:%M %p'))
#
class Person:
	def __init__(self, name, dob):
		self.name = name
		self.dob = dob

	def __repr__(self):
		print('__repr__ called...')
		return f'Person(name={self.name}, dob={self.dob.isoformat()})'

	def __str__(self):
		print('__str__ called...')
		return f'Person({self.name})'

	def __format__(self, date_format_spec):
		print(f'__format__ called with spec={date_format_spec}...')
		dob = format(self.dob, date_format_spec)
		return f'Person(name{self.name}, dob={dob})'

from datetime import date
p = Person('Alex', date(1900, 10, 20))
print(str(p))
print(repr(p))
print(format(p, '%B %d, %Y'))
print(format(p.dob))
print(str(p.dob))