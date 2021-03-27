#
#'''Docstring and Anonotations'''
#
#
# def my_func(a, b=1):
# 	# return a * b
# 	'''returns a x b
# 	Inputs:
#
# 	Outputs:
#
# 	'''
# 	return a * b
# print(help(my_func))
# print(my_func.__doc__)
# def my_func(a: 'annotation for a', 
# 	b: 'annotation for b' = 1) -> 'Smoething with a long anotation':
# 	'''Documentation for my_func'''
# 	return a * b
# print(help(my_func))
# print(my_func.__annotations__)
# x = 3
# y = 5
# def my_func(a: 'some character', b= max(x, y)) -> 'character a repeated ' + str(max(x, y)) + ' times':
# 	print(b)
# 	return a * max(x, y)
# print(my_func('a'))
# print(my_func.__annotations__)
# x = 10
# print(my_func('a'))
#
# def my_func(a: str,
# 	b: 'int > 0' = 1,
# 	*args: 'some extra positional args',
# 	k1: 'keyword-only arg 1',
# 	k2: 'keyword-only arg 2' = 100,
# 	**kwargs: 'some extra keyword-only args') -> 'something':
# 	print(a, b, args, k1, k2, kwargs)
# help(my_func)
# print(my_func.__annotations__)
# print(my_func(1, 2, 3, 4, 5, k1=10, k3=300, k4=400))
#
#'''Lambda Expressions'''
#
# def sq(x):
# 	return x**2
# print(type(sq))
# print(sq)
# print(lambda x: x**2)
# print(lambda x, y: x+y)
# f = sq
# print(id(f), id(sq))
# print(f(3), sq(3))
# print(f)
# f = lambda x: x**2
# print(f)
# print(f(3))
# g = lambda x, y=10: x+y
# print(g)
# print(g(1, 2))
# print(g(1))
# f = lambda x, *args, y, **kwargs: (x, args, y, kwargs)
# print(f(1, 'a', 'b', y=100, a=10, b=20))
# def apply_func(x, fn):
# 	return fn(x)
# print(apply_func(3, sq))
# print(apply_func(5, lambda x: x**2))
# print(apply_func(5, lambda x: x**3))
# def apply_func(fn, *args, **kwargs):
# 	return fn(*args, **kwargs)
# print(apply_func(sq, 3))
# print(apply_func(lambda x: x**2, 3))
# print(apply_func(lambda x, y: x+y, 1, 2))
# print(apply_func(lambda x, *, y: x+y, 1, y=20))
# print(apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5))
# print(apply_func(sum, (1,2,3,4,5)))
# print(sum((1,2,3,4,5)))
#
#'''Lambda and Sorting'''
#
# l = [1, 5, 4, 10, 9, 6]
# print(sorted(l))
# print(l)
# l = ['c', 'B', 'D', 'a']
# print(sorted(l))
# print(ord(('a')))
# print(ord(('c')))
# print(ord(('B')))
# print(sorted(l, key=lambda s: s.upper()))
# d = {'def': 300, 'abc': 200, 'ghi': 100}
# print(d)
# for i in d:
# 	print(i)
# print(sorted(d))
# print(sorted(d, key=lambda e:  d[e]))
# def dist_sq(x):
# 	return (x.real)**2 + (x.imag)**2
# print(dist_sq(1+1j))
# l = [3+3j, 1-1j, 0, 3]
# # print(sorted(l)) error
# print(sorted(l, key=dist_sq))
# print(sorted(l, key=lambda x: (x.real)**2 + (x.imag)**2 ))
# l = ['Cleese', 'Idle', 'Palin', 'Champan', 'Giliam', 'Jones']
# print(sorted(l))
# print(sorted(l, key=lambda s: s[-1]))
# import random
# help(random.random)
# print(random.random())
# l = [1,2,3,4,6,7,8,9,10]
# print(sorted(l, key=lambda x: random.random()))
#
#'''Function Introspection'''
#
#
# # TODO: Fix function
# def my_func(a: 'manadotary positional',
# 	b: 'optional positional=2',
# 	c=2, 
# 	*args: 'add extra positional here',
# 	kw1, 
# 	kw2=100, 
# 	kw3=200, 
# 	**kwargs):
# 	'''This function does nothing but does have various parameters 
# 	and annotations.
# 	'''
# 	i=10
# 	j=20
# print(my_func.__doc__)
# print(my_func.__annotations__)
# my_func.short_description = 'This is a function that does nothing much'
# print(my_func.short_description)
# print(dir(my_func))
# print(id(my_func))
# def func_call(f):
# 	print(id(f))
# 	print(f.__name__)
# print(func_call(my_func))
# print(my_func.__defaults__)
# print(my_func.__kwdefaults__)
# print(my_func.__code__)
# print(dir(my_func.__code__))
# print(my_func.__code__.co_name)
# print(my_func.__code__.co_varnames)
# print(my_func.__code__.co_argcount)
# import inspect
# from inspect import isfunction, ismethod, isroutine
# a = 10
# print(isfunction(10))
# print(isfunction(my_func))
# print(ismethod(my_func))
# class MyClass:
# 	def f(self):
# 		pass
# print(isfunction(MyClass.f))
# my_ojb = MyClass()
# print(isfunction(my_ojb))
# print(ismethod(my_ojb.f))
# inspect.getsource(my_func)
# print(inspect.getmodule(my_func))
# print(inspect.getmodule(print))
# print(inspect.getcomments(my_func))
# print(inspect.signature(my_func))
# print(dir(inspect.signature(my_func)))
# print(my_func.__annotations__)
# print(inspect.signature(my_func).return_annotation)
# sig = inspect.signature(my_func)
# print(sig)
# print(sig.parameters)
# for param in sig.parameters.values():
# 	print('Name: ', param.name)
# 	print('default:', param.default)
# 	print('Annotation:', param.annotation)
# 	print('Kind', param.kind)
# 	print('-----------------')
# 	
#'''Callables'''
#
# print(callable(print))
# print("world")
# result = print("hello")
# print(result)
# l = [1, 2, 3]
# print(callable(l.append))
# result = l.append(4)
# print(l)
# print(result)
# s = 'abc'
# result = s.upper()
# print(result)
# from decimal import Decimal
# print(callable(Decimal))
# a = Decimal('10.5')
# print(a)
# print(type(a))
# print(callable(a))
# class MyClass:
# 	def __init__(self, x=0):
# 		print('initializing...')
# 		self.counter = x
# 	def __call__(self, x=1):
# 		print('updating counter...')
# 		self.counter += x
# print(callable(MyClass))
# a = MyClass(100)
# print(a.counter)
# print(callable(a))
# b = MyClass()
# MyClass.__call__(b, 10)
# print(b.counter)
# print(callable(b))
# b(100)
# print(b.counter)
# print(type(MyClass))
# print(type(Decimal))
#
#'''Map, Filter, Zip and List Comprehensions'''
#
# def fact(n):
# 	return 1 if n < 2 else n * fact(n-1)
# print(fact(3))
# print(fact(4))
# result = list(map(fact, range(6)))
# print(result)
# l1 = [1, 2, 3, 4, 5]
# l2 = [10, 20, 30]
# l3 = [100, 200, 300, 400]
# result = list(map(lambda x, y, z: x+y+z, l1, l2, l3))
# print(result)
# result = map(lambda x, y: x+y, l1, l2, l3)
# print(result)
# # for x in result:
# # 	print(x)
# x = range(25)
# print(x)
# for i in x:
# 	print(i)
# for i in x:
# 	print(i)
# print(list(filter(lambda x: x % 3 == 0, range(25))))
# print(list(filter(None, [1, 0, 4, 'a', '', None, True, False])))
# l1 = [1, 2, 3, 4]
# l2 = [10, 20, 30, 40]
# l3 = 'python'
# result = list(zip(l1, l2, l3)) # if not list only once time callable.
# print(result)
# for x in result:
# 	print(x)
# for x in result:
# 	print(x)
# print(list(zip(range(10000), 'python')))
# l = range(10)
# print(list(l))
# print(list(map(fact, l)))
# result = [fact(n) for n in range(10)]
# print(result)
# result = (fact(n) for n in range(10))
# print(result)
# for x in result:
# 	print(x)
# l1 = [1, 2, 3, 4, 5, 6]
# l2 = [10, 20, 30, 40]
# print(list(map(lambda x, y: x+y, l1, l2)))
# print([x+y for x, y in zip(l1, l2)])
# print(list(filter(lambda x: x % 2 == 0, map(lambda x, y: x+y, l1, l2))))
# print([x+y for x, y in zip(l1, l2) if (x+y)%2 == 0])
#
#'''Reducing Functions'''
#
# l = [5, 8, 6, 10, 9]
# _max = lambda x, y: x if x> y else y
# def max_sequence(sequence):
# 	result = sequence[0]
# 	for x in sequence[1:]:
# 		result = _max(result, x)
# 	return result
# print(max_sequence(l))
# _min = lambda a, b: a if a < b else b
# def min_sequence(sequence):
# 	result = sequence[0]
# 	for x in sequence[1:]:
# 		result = _min(result, x)
# 	return result
# print(min_sequence(l))
# _add = lambda a, b: a + b
# def add_sequence(sequence):
# 	result = sequence[0]
# 	for x in sequence[1:]:
# 		result = _add(result, x)
# 	return result
# print(add_sequence(l))
# def _reduce(fn, sequence):
# 	result = sequence[0]
# 	for x in sequence[1:]:
# 		result = fn(result, x)
# 	return result
# print(_reduce(_max, l))
# print(_reduce(_add, l))
# from functools import reduce
# print(reduce(_max, l))
# print(reduce(_add, l))
# print(reduce(_max, {1, 2, 3, 4, 5}))
# print(min(l))
# print(min({1, 2, 3}))
# print(max(l))
# print(sum(l))
# print(sum({1, 2, 3}))
# s = {True, 1, 0, None}
# print(bool(True) and bool(1) and bool(0) and bool(None))
# print(all(s))
# s2 = {True, 1, "s"}
# print(all(s2))
# print(bool(True) and bool(1) and bool('s'))
# print(any(s2))
# s3 = {False, 0, '', None}
# print(any(s3))
# print(reduce(lambda a, b: bool(a) and bool(b), s))
# print(reduce(lambda a, b: bool(a) or bool(b), s3))
# l = [5, 8, 6, 10, 9]
# print(reduce(lambda a, b: a * b, l))
# print(range(5))
# print(range(5)[0])
# print(list(range(5)))
# print(list(range(1, 5+1)))
# print(reduce(lambda a, b: a * b, range(1, 5+1)))
# def fact(n):
# 	return 1 if n < 2 else n * fact(n-1)
# print(fact(5))
# def fact(n):
# 	return reduce(lambda a, b: a * b, range(1, n+1))
# print(fact(5))
# def _reduce(fn, sequence, initial):
# 	result = initial
# 	for x in sequence:
# 		result = fn(result, x)
# 	return result
# print(l)
# print(_reduce(lambda a, b: a+b, l, 1))
# print(_reduce(lambda a, b: a+b, {1,2,3,4}, 100))
# print(reduce(lambda a, b: a+b, l, 100))
#
#'''Partial Functions'''
#
# from functools import partial
# def my_func(a, b, c):
# 	print(a, b, c)
# my_func(10, 20, 30)
# def f(x, y):
# 	return my_func(10, x, y)
# f(20, 30)
# f(100, 200)
# f = lambda x, y: my_func(10, x, y)
# f(100, 200)
# f = partial(my_func, 10)
# f(20, 30)
# f = partial(my_func, 10, 20)
# f(30)
# def my_func(a, b, *args, k1, k2, **kwargs):
# 	print(a, b, args, k1, k2, kwargs)
# my_func(10, 20, 100, 200, k1='a', k2='b', k3=2300, k4=200)
# def f(x, *args, kw, **kwargs):
# 	return my_func(10, x, *args, k1='a', k2=kw, **kwargs)
# f(20, 100, 200, kw='b', k3='10000', k4=200000)
# f = partial(my_func, 10, k1='a')
# f(20, 100, 200, k2='b', k3=10000, k4=403024)
# def pow(base, exponent):
# 	return base ** exponent
# sq = partial(pow, exponent=2)
# print(sq(10))
# cu = partial(pow, exponent=3)
# print(cu(5))
# a = 2
# sq = partial(pow, exponent=a)
# print(sq(5))
# def my_func(a, b):
# 	print(a, b)
# a = [1, 2]
# f = partial(my_func, a)
# a.append(3)
# print(a)
# f(100)
# origin = (0, 0)
# l = [(1, 1), (0, 2), (-3, 2), (0, 0), (10, 10)]
# print(l)
# dist2 = lambda a, b: (a[0] - b[0])**2 + (a[1] - b[1])**2
# dist2((1, 1), origin)
# print(sorted(l))
# f = partial(dist2, origin)
# f((1,1))
# print(sorted(l, key=f))
# f= lambda x: dist2(origin, x)
# print(sorted(l, key=f))
# print(sorted(l, key=lambda x: dist2(origin, x)))
#
#'''The operator module'''
#
# import operator
# print(operator.add(1, 2))
# print(operator.mul(2, 3))
# print(operator.truediv(3, 2))
# print(operator.floordiv(13, 2))
# print(13//2)
# from functools import reduce
# print(reduce(lambda x, y: x*y, [1, 2, 3, 4]))
# print(reduce(operator.mul, [1, 2, 3, 4]))
# print(operator.lt(10, 3))
# print(operator.is_('abc', 'def'))
# from operator import is_
# print(is_('abc', 'def'))
# print(is_('abc', 'abc'))
# print(operator.truth([]))
# print(operator.truth([1]))
# my_list = [1, 2, 3, 4]
# print(my_list[1])
# print(operator.getitem(my_list, 1))
# operator.setitem(my_list, 1, 100)
# print(my_list)
# operator.delitem(my_list, 3)
# print(my_list )
# f = operator.itemgetter(2)
# print(type(f))
# my_list = [1, 2, 3, 4]
# print(f(my_list))
# s = 'python'
# print(f(s))
# f = operator.itemgetter(2, 3)
# print(type(f))
# my_list = [1, 2, 3, 4]
# print(f(my_list))
# print(f('python'))
# class MyClass:
# 	def __init__(self):
# 		self.a = 10
# 		self.b = 20
# 		self.c = 30
#
# 	def test(self):
# 		print('test method running...')
# obj = MyClass()
# print(obj)
# print(obj.a, obj.b, obj.c, obj.test)
# print(obj.test())
# prop_a = operator.attrgetter('a')
# print(prop_a(obj))
# my_var = 'b'
# print(operator.attrgetter(my_var)(obj))