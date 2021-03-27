#
#'''Positional and Keyword Arguments 
#
# def my_func(a, b, c):
# 	print(f'a={a}, b={b}, c={c}')
# my_func(1, 2, 3)
#
# def my_func(a=1, b=2, c=3):
# 	print(f'a={a}, b={b}, c={c}')
#
# my_func(10, 20, 30)
# my_func(10, 20)
# my_func(10)
# my_func()
#
# def my_func(a, b=2, c=3):
# 	print(f'a={a}, b={b}, c={c}')
# my_func(c=30, b=20, a=10)
# my_func(10, c=30, b=20)
# my_func(10, c=30)
#
#'''Unpacking Iterables'''
#
# a = (1, 2, 3)
# print(type(a))
# a = 1, 2, 3
# print(type(a))
# a = ('a')
# print(a)
# print(type(a))
# a = (1, )
# print(a)
# print(type(a))
# a = ()
# print(type(a))
# a, b, c = [1, 'a', 3.14]
# print(a, b, c)
# (a, b, c) = [1, 2, 3]
# print(a, b, c)
# (a, b) = (1, 2)
# print(a, b)
# a, b = 10, 20
# a, b, c = 10, 20, 30
# print(a, b, c)
# a, b, c = 10, 'a', 3.14
# a, b, c = 10, {1, 2}, ['a', 'b']
# print(a)
# print(b)
# print(c)
# a, b = 10, 20
# print(a, b)
# a, b = b, a
# print(a, b)
# for e in 'XYZ':
# 	print(e)
# a, b, c = 'XYZ'
# print(a, b, c)
# s = 'XYZ'
# print(s[1])
# s = {1, 2, 3}
# print(s[1]) TypeError: 'set' object is not subscriptable
# s = {'p', 'y', 't', 'h', 'o', 'n'}
# print(s)
# for e in s:
# 	print(e)
# a, b, c, d, e, f = s
# print(a, b)
# d = {'a': 1, 'b': 2, 'c': 3}
# for e in d:
# 	print(e)
# a, b, c = d
# print(d)
#
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(d)
# a, b, c, d = d
# print(a)
# print(d)
#
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(d)
# d, a, b, c = d
# print(d, a)
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print("Keys")
# for e in d:
# 	print(e)
# print("Values")
# for e in d.values():
# 	print(e)
# a, b, c, d = d.values()
# print(a, b, c, d)
#
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for e in d.items():
# 	print(e)
# # unpacking
# for e in d.items():
# 	a, b = e
# 	print(f'key={a}, value={b}')
# #	
# for a, b in d.items():
# 	print(f'key={a}, value={b}')
#
#'''Extended Unpacking'''
# l = [1, 2, 3, 4, 5, 6]
# a = l[0]
# b = l[1:]
# print(a)
# print(b)
# print("Unpacking")
# a, b = l[0], l[1:]
# print(a)
# print(b)
# a, *b = l
# print(a, "|", b)
# s = {1, 2, 3}
# s = 'python'
# a, *b = s # *b returns list
# print(a)
# print(b)
#
# t = ('a', 'b', 'c') 
# a, *b = t
# print(a, b) # *b always returns list
# [a, b, c] = 'XYZ'
# print(a)
# print(b)
# print(c)
# s = 'python'
# a, b, *c = 'python'
# print(a, b, c)
# a, b, *c, d = s
# print(a, b, c, d)
#
# s = 'python'
# a, b, c, d = s[0], s[1], s[2:-1], s[-1]
# print(a, b, c, d)
# *c, = c
# print(c)
# print(a, b, list(c), d)
# print(c)
# print("Unpacking")
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l = [*l1, *l2]
# print(l)
# l1 = [1, 2, 3]
# s = 'abc'
# print([*l1, *s])
# l1 = [1, 2, 3]
# s1 = {'x', 'y', 'z'}
# print([*l1, *s1])
# s1 = 'abc'
# s2 = 'cde'
# print([*s1, *s2])
# print({*s1, *s2})
# s = {10, -99, 3, 'd'}
# for c in s:
# 	print(c)
# a, b, *c = s
# print(a, c)
# print(list(s))
# *c, =s
# print(c)
# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# c = {*s1, *s2} # = s1.union(s2) ; print(help(set))
# print(c)
# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s3 = {5, 6, 7}
# s4 = {7, 8, 9}
# print(s1.union(s2).union(s3).union(s4))
# print(s1.union(s2, s3, s4))
# print([*s1, *s2, *s3, *s4])
# print({*s1, *s2, *s3, *s4})
# d1 = {'key1': 1, 'key2': 2}
# d2 = {'key2': 3, 'key4': 4}
# print({*d1, *d2})
# print({**d1, **d2})
# print({**d2, **d1})
# print({'a': 1, 'b': 2, **d1, 'c': 3})
# a, b, e = [1, 2, 'XY']
# print(a, b, e)
# c, d = e
# print(c, d)
# a, b, (c, d) = [1, 2, 'XY']
# print(a, b, c, d)
# a, *b, (c, d, *e) = [1, 2, 3, 'python']
# print(a)
# print(b)
# print(c, d, e)
# print('unpacking')
# l = [1, 2, 3, 'python']
# a, *b, (c, d, *e) = l
# print(a, b, c, d, e)
# print('slicing')
# print(l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:]))
# a, b, c, d, e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
# print(a, b, c, d, e)
# l = (1, 2, 3, 4, ['a', 'b', 'c', 'd'])
# a, *b, (c, d, *e) = l
# print(a, b, c, d, e)
#
#'''args'''
#
# print("Unpacking")
# a, b, *c = 10, 20, 'a', 'b'
# print(a, b, c)
# def func1(a, b, *args):
# 	print(a)
# 	print(b)
# 	print(args)
# func1(10, 20)
# func1(10, 20, 1, 2, 3)
# def avg(*args):
# 	print(args)
# avg()
# avg(10, 20)
# def avg(*args):
# 	count = len(args)
# 	total = sum(args)
# 	return total/count
# print(avg(2, 2, 4, 4))
# def avg(*args):
# 	count = len(args)
# 	total = sum(args)
# 	if count == 0:
# 		return 0
# 	return total/count
# print(avg())
# print(avg(2, 2, 4, 4))
# def avg(*args):
# 	count = len(args)
# 	total = sum(args)
# 	return count and total/count # fix zero division error same to if/else
# print(avg(2, 2, 4, 4))
# def avg(a, *args): # bad idea.
# 	count = len(args) + 1
# 	total = sum(args) + a
# 	return total/count
# print(avg(2, 2, 4, 4))
# def func1(a, b, c, *args):
# 	print(a)
# 	print(b)
# 	print(c)
# 	print(args)
# l = [10, 20, 30, 40, 50]
# func1(*l)
#
#'''keyword arguments'''
# def func1(a, b, c):
# 	print(a, b, c)
# func1(1, 2, 3)
# func1(1, c=3, b=2)
# func1(c=3, b=2, a=1)
# def func1(a, b, *args):
# 	print(a, b, *args)
# func1(1, 2, 3, 4)
# def func1(a, b, *args, d):
# 	print(a, b, args, d)
# func1(1, 2, 3, 4, d=5) # if not d=... TypeError: func1() missing 1 required keyword-only argument: 'd'
# def func1(*args, d):
# 	print(args, d)
# func1(1,2, 3, d='a')
# func1(d='a')
# def func(*, d):
# 	print(d)
# func(d=100)
# def func(a, b, *, d):
# 	print(a, b, d)
# func(1, 2, d=4)
# def func(a, b=2, *args, d):
# 	print(a, b, args, d)
# func(1, 5, 3, 4, d='a')
# def func(a, b, *args, d=0, e):
# 	print(a, b, args, d, e)
# func(5, 4, 3, 2, 1, e= 'all engines running')
# func(0, 600, d='heeeeelpp', e='deep dive')
# func(11, 'm/s', 24, 'mph', d='unladen', e='swallow')
#
#'''kwargs'''
#
# def func(**others):
# 	print(others)
# func(a=1, b=2, c=3)
# def func(*args, **kwargs):
# 	print(args)
# 	print(kwargs)
# func(1, 2, x=100, y=200)
# def func(a, b, *, d, **kwargs):
# 	print(a)
# 	print(b)
# 	print(d)
# 	print(kwargs)
# func(1, 2, x=100, y=200, d=20)
# def func(a, b, **kwargs):
# 	print(a)
# 	print(b)
# 	print(kwargs)
# func(1, 2, x=100, y=200)
#
#'''Putting it all together'''
#
# def func(a, b, *args):
# 	print(a, b, args)
# func(1, 2, 'x', 'y', 'z')
# #func(a=1, b=2, 'x', 'y', 'z') #error
# def func(a, b=2, c=3, *args):
# 	print(a, b, c, args)
# func(1, 2, 3, 'x', 'y', 'z')
# def func(a, b=2, *args, c=3, d):
# 	print(a, b, args, c, d)
# func(10, 20, 'x', 'y', 'z', d=5)
# func(1, 3, 'x', 'y', 'z', d=13)
# def func(a, b, *args, c=10, d=20, **kwargs):
# 	print(a, b, args, c, d, kwargs)
# func(1, 2, 'x', 'y', 'z', c=100, d=200, x=0.1, y=0.2)
# print(1, 2, 3, sep='-')
# print(1,2,3,4, end=' *** ')
# print(1,2,3,4)
# def calc_hi_lo_avg(*args, log_to_console=False):
# 	hi = int(bool(args)) and max(args)
# 	lo = min(args) if len(args) > 0 else 0 
# 	avg = (hi + lo) / 2
# 	if log_to_console:
# 		print(f"High={hi}, low={lo}, avg={avg}")
# 	return avg
#
# is_debug = True
# avg = calc_hi_lo_avg(1, 2, 3, 4, log_to_console= is_debug)
# print(avg)
#
#'''Application A simple Function timer'''
#
# def time_it(func, *args, **kwargs):
# 	print(args, kwargs)
# time_it(print, 1, 2, 3, sep=' - ', end=' ***')
#
# def time_it(func, *args, rep=1, **kwargs):
# 	for i in range(rep):
# 		func(*args, **kwargs)
# time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)
# import time
# def time_it(func, *args, rep=1, **kwargs):
# 	start = time.perf_counter()
# 	for i in range(rep):
# 		func(*args, **kwargs)
# 	end = time.perf_counter()
# 	return (end - start) / rep
# print(time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5))
# import time
# def compute_powers_1(n, *, start=1, end):
# 	# using for loop
# 	results = []
# 	for i in range(start, end):
# 		results.append(n**i)
# 	return results
# print(compute_powers_1(2, end=5))
#
# def compute_powers_2(n, *, start=1, end):
# 	# using a list comprehension
# 	return [n**i for i in range(start, end)]
# print(compute_powers_2(2, end=5))
#
# def compute_powers_3(n, *, start=1, end):
# 	# using generators expression
# 	return (n**i for i in range(start, end))
# print(list(compute_powers_3(2, end=5)))
# print(time_it(compute_powers_1, 2, end=20000, rep=5))
# print(time_it(compute_powers_2, 2, end=20000, rep=5))
# print(time_it(compute_powers_3, n=2, end=20000, rep=5))
#
# a = (2**i for i in range(5))
# print(list(a))
#
#'''Parameter Defaults'''
#
# from datetime import datetime
# print(datetime.utcnow())
# def log(msg, *, dt=datetime.utcnow()):
# 	print(f'{dt} : {msg}')
# log("Message 1", dt='2001-01-01 00:00')
# log('Message 2')
# log('Message 3')
# def log(msg, *, dt=None):
# 	dt = dt or datetime.utcnow()
# 	# if not dt:
# 	# 	dt = datetime.utcnow()
# 	print(f'{dt} : {msg}')
# log('Message 1', dt='2000-01-02 00:00')
# log('Message 2')
# my_list = [1, 2, 3]
# def func(a=my_list):
# 	print(a)
# func()
# func(['a, b'])
# def add_item(name, quantity, unit, grocery_list):
# 	grocery_list.append(f'{name} ({quantity} {unit})')
# 	return grocery_list
# store1 = []
# store2 = []
# add_item('banana', 2, 'units', store1)
# add_item('milk', 1, 'liter', store1)
# print(store1)
# add_item('python', 1, 'medium-rare', store2)
# print(store2)
# print("MISTAKE")
# print("---------------")
# def add_item(name, quantity, unit, grocery_list=[]):
# 	grocery_list.append(f'{name} ({quantity} {unit})')
# 	return grocery_list
# store1 = add_item('banana', 2, 'units')
# add_item('milk', 1, 'liter', store1)
# print(store1)
# store2 = add_item('python', 1, 'medium-rare')
# print(store2)
# print(store1)
# print(store1 is store2)
# print("---------------")
# def add_item(name, quantity, unit=1, grocery_list=None):
# 	if not grocery_list:
# 		grocery_list = []
# 	grocery_list.append(f'{name} ({quantity} {unit})')
# 	return grocery_list
# store1 = add_item('banana', 2, 'units')
# add_item("milk", 1, 'liter', store1)
# print(store1)
# store2 = add_item('Python', 1, 'medium-rare')
# print(store2)
# print(store1 is store2)
# def factorial(n):
# 	if n <1:
# 		return 1
# 	else:
# 		print(f"calculating {n}!")
# 		return n *factorial(n-1)
# print(factorial(3))
# def factorial(n, *, cache):
# 	if n <1:
# 		return 1
# 	elif n in cache:
# 		return cache[n]
# 	else:
# 		print(f"calculating {n}!")
# 		result =  n * factorial(n-1, cache=cache)
# 		cache[n] = result
# 		return result
# cache={}
# print(factorial(3, cache=cache))
# print(cache)
# print(factorial(4, cache=cache))
# print(cache)
