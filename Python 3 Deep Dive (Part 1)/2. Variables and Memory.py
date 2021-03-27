# '''memory'''
# my_var = 10
# print(my_var)
# print(id(my_var))
# print(hex(id(my_var)))
#
# greeting = 'hello'
# print(greeting)
# print(id(greeting))
# print(hex(id(greeting)))
#
#'''reference counting'''
# import sys
# a = [1, 2, 3 ]
# print(id(a))
# print(sys.getrefcount(a))
# import ctypes
# def ref_count(address :int):
# 	return ctypes.c_long.from_address(address).value
# print(ref_count(id(a)))
# c = a
# print(ref_count(id(a)))
# c = 10 
# print(ref_count(id(a)))
# a_id = id(a)
# a = None
# print(ref_count(a_id))
# 
#'''Garbage Colection'''
# import ctypes
# import gc
#
# def ref_count(address):
# 	return ctypes.c_long.from_address(address).value
#
# def object_by_id(object_id):
# 	for obj in gc.get_objects():
# 		if id(obj) == object_id:
# 			return "Object exists"
# 	return "Not Found"
#
# class A:
# 	def __init__(self):
# 		self.b = B(self)
# 		print(f"A: self {hex(id(self))}, b: {hex(id(self.b))}")
#
# class B:
# 	def __init__(self, a):
# 		self.a = a
# 		print(f"B: self {hex(id(self))}, a: {hex(id(self.a))}")
#
# gc.disable()
# my_var = A()
#
# print(hex(id(my_var)))
# print(hex(id(my_var.b)))
# print(hex(id(my_var.b.a)))
#
# a_id = id(my_var)
# b_id = id(my_var.b)
#
# print(hex(a_id))
# print(hex(b_id))
#
# print(ref_count(a_id))
# print(ref_count(b_id))
#
# print(object_by_id(a_id))
# print(object_by_id(b_id))
#
# my_var = None
#
# print(ref_count(a_id))
# print(ref_count(b_id))
#
# print(object_by_id(a_id))
# print(object_by_id(b_id))
#
# print(gc.collect())
#
# print(object_by_id(a_id))
# print(object_by_id(b_id))
#
# print(ref_count(a_id))
# print(ref_count(b_id))
#'''Dynamic vs static Typing 
# a = "Hello"
# print(type(a))
# a = 10
# print(type(a))
# a = lambda x: x**2
# a(2)
# print(type(a))
# a = 3 + 4j
# print(type(a))
#
#'''Variable RE-assignment '''
# a = 10
# print(hex(id(a)))
# print(type(a))
#
# a = 15
# print(hex(id(a)))
#
# a = a + 1
# print(hex(id(a)))
#
# a = 10
# b = 10
# print(hex(id(a)))
# print(hex(id(b)))
#'''object mutability'''
# my_dict = {'key1': 1, 'key2': 'a'}
# print(my_dict)
# print(id(my_dict))
# my_dict['key3'] = 10.5
# print(my_dict)
# print(id(my_dict))
# t = (1, 2, 3)
# print(t)
# print(id(t))
# print(id(t[1]))
# t = ([1, 2], [3,4])
# print(t)
# print(id(t))
# print(t[0])
# t[0].append(3)
# print(t)
#'''Function Arguments And Mutability'''
# def process(s):
# 	print(f'initial s # = {id(s)}')
# 	s = s + 'world'
# 	print(f'Final s # = {id(s)}')
#
# my_var = 'hello'
# print(f'my_var # = {id(my_var)}')
# process(my_var)
# print(id(my_var))
# def modify_list(lst):
# 	print(f'initial lst # = {id(lst)}')
# 	lst.append(100)
# 	print(f'Final lst # = {id(lst)}')
# my_list = [1, 2, 3]
# print(modify_list(my_list)) 
# print(id(my_list))
# print(my_list)
#
# def modify_tuple(t):
# 	print(f"Initial t # {id(t)}")
# 	t[0].append(100)
# 	print(f'Final t # = {id(t)}')
# my_tuple = ([1, 2], 'a')
# print(id(my_tuple))
# print(modify_tuple(my_tuple))
#'''SHARED REFERENCES AND MUTABILITY'''
# a = 10
# b = a
# print(id(a))
# print(id(b))
# a = 'hello'
# b = a
# print(hex(id(a)))
# print(hex(id(b)))
# a = 'hello'
# b = 'hello'
# print(hex(id(a)))
# print(hex(id(b)))
# b = 'hello world'
# print(hex(id(b)))
# print(hex(id(a)))
#
# a = [1, 2, 3]
# b = a
# print(hex(id(a)))
# print(hex(id(b)))
# b.append(100)
# print(hex(id(a)))
# print(hex(id(b)))
# print(a)
# print(b)
# a = 500
# b = 500
# print(hex(id(a)))
# print(hex(id(b)))
#'''VARIABLE EQUALITY'''
#
# a = 10
# b = 10
# print(id(a))
# print(id(b))
# print("a is b", a is b)
# print("a == b", a == b)
#
# a = 500
# b = 500
# print(id(a))
# print(id(b))
# print("a is b", a is b)
# print("a == b", a == b)
#
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a))
# print(id(b))
# print("a is b", a is b)
# print("a == b", a == b)
#
# a = 10
# b = 10.0
# print(id(a))
# print(id(b))
# print("a is b", a is b)
# print("a == b", a == b)
#
# a = 10 + 0j
# b = 500
# print(id(a))
# print(id(b))
# print("a is b", a is b)
# print("a == b", a == b)
#
# print(id(None))
# a = None
# b = None
# c = None
# print(a is b)
# print(a is c)
# print(a is None)
# print(b is None)
# print(c is None)
#
#'''Everything is an Object'''
#
# a = 10
# print(type(a))
# b = int(10)
# print(b)
# print(type(b))
#
#help(int)
# c = int()
# print(c)
# c = int('101', base=2)
# print(c)
#
# def square(a):
# 	return a ** 2
# print(type(square))
# f = square
# print(id(square))
# print(id(f))
# print(f is square)
# square(2)
# print(square(2))
#
# def square(a):
# 	return a ** 2
# def cube(a):
# 	return a ** 3
# def select_function(fn_id):
# 	if fn_id == 1:
# 		return square
# 	else:
# 		return cube
# f = select_function(1)
# print(f is square)
# print(f(2))
# f = select_function(2)
# f is cube
# print(select_function(2)(3))
#
# def square(a):
# 	return a ** 2
# def cube(a):
# 	return a ** 3
# def exec_function(fn, n):
# 	 return fn(n)
# print(exec_function(cube, 3))
# print(exec_function(square, 3))
# [-5, 256]
# a = 10
# b = 10
# print(id(a))
# print(id(b))
# a = -5
# b = -5
# print(id(a), id(b))
# print(a is b)
# a = 257
# b = 257
# print(a is b)
# a = 10
# b = int(10)
# c = int('10')
# d = int('1010', 2)
# print(a, b, c, d)
# print(id(a), id(b), id(c), id(d))
#
#'''Python Optimizations String Interning'''
#
# a = 'hello'
# b = 'hello'
# print(id(a), id(b))
# print(a == b)
# print(a is b)
# a = 'hello world'
# b = 'hello world'
# print(id(a), id(b))
# print(a is b)
# print(a == b)
# a = '_this_is_a_long_string_that_colud_be_user_as_an_identifier'
# b = '_this_is_a_long_string_that_colud_be_user_as_an_identifier'
# print(a is b)
#
# import sys
# a = sys.intern('hello bekha')
# b = sys.intern('hello bekha')
# c = 'hello bekha'
# print(id(a), id(b), id(c))
# print(a == b)
# print(a is b)
#
# def compare_using_equals(n):
# 	a = 'a long string that is not interned' * 200
# 	b = 'a long string that is not interned' * 200
# 	for i in range(n):
# 		if a == b:
# 			pass

# def compare_using_interning(n):
# 	a = sys.intern('a long string that is not interned' * 200)
# 	b = sys.intern('a long string that is not interned' * 200)
# 	for i in range(n):
# 		if a is b:
# 			pass
# import time
# start = time.perf_counter()
# compare_using_equals(10000000)
# end = time.perf_counter()
# print('EQUALITY', end-start)
# import time
# start = time.perf_counter()
# compare_using_interning(10000000)
# end = time.perf_counter()
# print('EQUALITY', end-start)
#
#'''Python Optimizations Peephole'''
#
# def my_func():
# 	a = 24 * 60
# 	b = (1, 2) * 5
# 	c = 'abc' * 3
# 	d = 'ab' * 11
# 	e = 'the quick brown fox' * 5
# 	f = ['a', 'b'] * 3
# print(my_func.__code__.co_consts)
#
# def my_func(e):
# 	if e in {1, 2, 3}:
# 		pass
# print(my_func.__code__.co_consts)
#
import string 
import time
print(string.ascii_letters)
char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)
print(char_list)
print(char_tuple)
print(char_set)
def membership_test(n, container):
	for i in range(n):
		if 'z' in container:
			pass
start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print('list:', end-start)
start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print('list:', end-start)
start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print('list:', end-start)