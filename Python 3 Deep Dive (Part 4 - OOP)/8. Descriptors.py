"""Descriptors"""

# from datetime import datetime

# class TimeUTC:
# 	def __get__(self, instance, owner_class):
# 		return datetime.utcnow().isoformat()


# class Logger:
# 	current_time = TimeUTC

# print(Logger.__dict__)

# print(Logger.current_time)
# l = Logger()
# print(l.current_time)

# from random import choice, seed

# class Deck:
# 	@property
# 	def suit(self):
# 		return choice(('Spade', 'Heart', 'Diamond', 'Club'))

# 	@property
# 	def card(self):
# 		return choice(tuple('23456789JQKA') + ('10', ))

# d = Deck()
# seed(0)

# for _ in range(10):
# 	print(d.card, d.suit)
	
# from random import choice, seed
# class Choice:
# 	def __init__(self, *choices):
# 		self.choices = choices

# 	def __get__(self, instance, owner_class):
# 		return choice(self.choices)

# class Deck:
# 	suit = Choice('Spade', 'Heart', 'Diamond', 'Club')
# 	card = Choice(*'23456789JQKA', '10')

# seed(0)
# d = Deck()
# for _ in range(10):
# 	print(d.card, d.suit)


# class Dice:
# 	die_1 = Choice(1, 2, 3, 4, 5, 6)
# 	die_2 = Choice(1, 2, 3, 4, 5, 6)
# 	die_3 = Choice(1, 2, 3, 4, 5, 6)
# seed(0)
# dice = Dice()
# for _ in range(10):
# 	print(dice.die_1, dice.die_2, dice.die_3)

from datetime import datetime

# class TimeUTC:
# 	def __get__(self, instance, owner_class):
# 		print(f'__get__ called, self={self}, instance={instance}, owner_class={owner_class}')
# 		return datetime.utcnow().isoformat()


# class Logger1:
# 	current_time = TimeUTC()


# class Logger2:
# 	current_time = TimeUTC()


# getattr(Logger1, 'current_time')
# print(Logger1.current_time)
# print(Logger2.current_time)

# class TimeUTC:
# 	def __get__(self, instance, owner_class):
# 		if instance is None:
# 			return self
# 		else:
# 			return datetime.utcnow().isoformat()


# class Logger:
# 	current_time = TimeUTC()


# print(Logger.current_time)
# l = Logger()
# print(l.current_time)


# Application - Example 1

# class Int:
# 	def __set_name__(self, owner_class, prop_name):
# 		self.prop_name = prop_name

# 	def __set__(self, instance, value):
# 		if not isinstance(value, int):
# 			raise ValueError(f'{self.prop_name} must be an integer.')
# 		instance.__dict__[self.prop_name] = value

# 		def __get__(self, instance, owner_class):
# 			if instance is None:
# 				return self
# 			else:
# 				return instance.__dict__.get(self.prop_name, None)

# class Float:
# 	def __set_name__(self, owner_class, prop_name):
# 		self.prop_name = prop_name

# 	def __set__(self, instance, value):
# 		if not isinstance(value, float):
# 			raise ValueError(f'{self.prop_name} must be an float.')
# 		instance.__dict__[self.prop_name] = value

# 		def __get__(self, instance, owner_class):
# 			if instance is None:
# 				return self
# 			else:
# 				return instance.__dict__.get(self.prop_name, None)

# class List:
# 	def __set_name__(self, owner_class, prop_name):
# 		self.prop_name = prop_name

# 	def __set__(self, instance, value):
# 		if not isinstance(value, list):
# 			raise ValueError(f'{self.prop_name} must be an list.')
# 		instance.__dict__[self.prop_name] = value

# 		def __get__(self, instance, owner_class):
# 			if instance is None:
# 				return self
# 			else:
# 				return instance.__dict__.get(self.prop_name, None)

# class Person:
# 	age = Int()
# 	height = Float()
# 	tags = List()
# 	favorite_foods = List()

# p = Person()
# try:
# 	p.tags = 'abcs'
# except ValueError as ex:
# 	print(ex)

# class ValidType:
# 	def __init__(self, type_):
# 		self._type = type_

# 	def __set_name__(self, owner_class, prop_name):
# 		self.prop_name = prop_name

# 	def __set__(self, instance, value):
# 		if not isinstance(value, self._type):
# 			raise ValueError(f'{self.prop_name} must be of type {self._type.__name__}')
# 		instance.__dict__[self.prop_name] = value

# 		def __get__(self, instance, owner_class):
# 			if instance is None:
# 				return self
# 			else:
# 				return instance.__dict__.get(self.prop_name, None)

# class Person:
# 	age = ValidType(int)
# 	height = ValidType(float)
# 	tags = ValidType(list)
# 	favorite_foods = ValidType(tuple)

# p = Person()
# try:
# 	p.age = 10.1
# except ValueError as ex:
# 	print(ex)

# import numbers

# print(isinstance(10, numbers.Real))

# class Person:
# 	age = ValidType(int)
# 	height = ValidType(numbers.Real )
# 	tags = ValidType(list)
# 	favorite_foods = ValidType(tuple)

# class Int:
# 	def __init__(self, min_value=None, max_value=None):
# 		self.min_value = min_value
# 		self.max_value = max_value

# 	def __set_name__(self, owner_class, name):
# 		self.name = name

# 	def __set__(self, instance, value):
# 		if not isinstance(value, int):
# 			raise ValueError(f'{self.name} must be an int')
# 		if self.min_value is not None and value < self.min_value:
# 			raise ValueError(f'{self.name} must be at least {self.min_value}')
# 		if self.max_value is not None and value > self.max_value:
# 			raise ValueError(f'{self.name} cannot be greater than {self.max_value}')
# 		instance.__dict__[self.name] = value

# 	def __get__(self, instance, owner_class):
# 		if instance is None:
# 			return self
# 		else:
# 			return instance.__dict__.get(self.name, None)

# class Point2D:
# 	x = Int(min_value=0, max_value=800)
# 	y = Int(min_value=0, max_value=600)

# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y

# 	def __repr__(self):
# 		return f'Point2D(x={self.x}, y={self.y})'

# 	def __str__(self):
# 		return f'({self.x}, {self.y})'

# p = Point2D(0, 10)
# print(p)
# print(repr(p))
# try:
# 	p = Point2D(0, 800)
# except ValueError as ex:
# 	print(ex)

# import collections

# class Point2DSequence:
# 	def __init__(self, min_length=None, max_length=None):
# 		self.min_length = min_length
# 		self.max_length = max_length

# 	def __set_name__(self, cls, name):
# 		self.name = name

# 	def __set__(self, instance, value):
# 		if not isinstance(value, collections.Sequence):
# 			raise ValueError(f'{self.name} must be a sequence type')
# 		if self.min_length is not None and len(value) < self.min_length:
# 			raise ValueError(f'{self.name} must containt at least {self.min_length} elements.')
# 		if self.max_length is not None and len(value) > self.max_length:
# 			raise ValueError(f'{self.name} must cannt contain more than {self.max_length} elements.')

# 		for index, item in enumerate(value):
# 			if not isinstance(item, Point2D):
# 				raise ValueError(f'Item at index {index} is not a Point2D instance.')
# 		instance.__dict__[self.name] = list(value)

# 	def __get__(self, instance, owner_class):
# 		if instance is None:
# 			return self
# 		else:
# 			if self.name not in instance.__dict__:
# 				instance.__dict__[self.name] = []
# 			#return instance.__dict__[self.name]
# 			return instance.__dict__.get(self.name)


# class Polygon:
# 	vertices = Point2DSequence(min_length=3)

# 	def __init__(self, *vertices):
# 		self.vertices = vertices


# try:
# 	p = Polygon()
# except ValueError as ex:
# 	print(ex)

# try:
# 	p = Polygon(Point2D(-100, 0), Point2D(0, 1), Point2D(1, 0))
# except ValueError as ex:
# 	print(ex)
