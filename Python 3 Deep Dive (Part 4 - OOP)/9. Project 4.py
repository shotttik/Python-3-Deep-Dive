import numbers

class IntegerField:
	def __init__(self, min_, max_):
		self._min = min_
		self._max = max_

	def __set_name__(self, owner_class, prop_name):
		self.prop_name = prop_name

	def __set__(self, instance, value):
		if not isinstance(value, numbers.Integral):
			raise ValueError(f'{self.prop_name} must be an integer value')
		if value < self._min:
			raise ValueError(f'{self.prop_name} must be >= {self._min}')
		if value > self._max:
			raise ValueError(f'{self.prop_name} must be <= {self._max}')
		instance.__dict__[self.prop_name] = value

	def __get__(self, instance, owner_class):
		if instance is None:
			return self
		return instance.__dict__(self.prop_name, None)

class Person:
	age = IntegerField(0, 100)

p = Person()
p.age = 5
try:
	p.age = 200
except ValueError as ex:
	print(ex)
