# ''' Objects and Classes - Coding'''
#
# class Person:
# 	pass
# print(type(Person))
# print(Person.__name__)
# p = Person()
# print(type(Person()))
# print(p.__class__)
# print(type(p) is p.__class__)
# print(isinstance(p, Person))
# print(isinstance(p, str))
# print(isinstance('hello', str))
# print(type(str))
#
# '''Class attributes'''
#
# class Person:
# 	pass
# print(Person.__name__)
# class Program:
# 	language = "Python"
# 	version = '3.6'
# print(Program.__name__)
# print(type(Program))
# print(Program.language)
# print(Program.version)
# Program.version = '3.7'
# print(Program.version)
# print(getattr(Program, 'version'))
# setattr(Program, 'version', '3.6')
# print(getattr(Program, 'version'))
# print(getattr(Program, 'x', 'N/A'))
# print(getattr('hello', 'x', 'n/a'))
# Program.x =100
# print(Program.x, getattr(Program, 'x'))
# setattr(Program, 'x', -100)
# print(Program.__dict__)
# print(Program.__dict__['language']) 
#
#'''Callable Class Attributes
#
# class Program:
# 	language = 'Python'
#
# 	def say_hello():
# 		print(f'Hello from {Program.language}')
#
# print(Program.__dict__)
# Program.say_hello(), getattr(Program, 'say_hello')
# Program.say_hello()
# getattr(Program, 'say_hello')()
# Program.__dict__['say_hello']()
#
#'''Classes are callable'''
#
# class Program:
# 	language = 'Python'
#
# 	def say_hello():
# 		print(f'Hello from {Program.language}')
#
# p = Program()
# print(type(p))
# print(isinstance(p, Program))
# print(p.__dict__)
# print(Program.__dict__)
# print(p.__class__)
# print(type(p) is p.__class__)
# class MyClass:
# 	pass
# m = MyClass()
# print(type(m), m.__class__)
# class MyClass:
# 	__class__ = str
# m = MyClass()
# print(m.__class__, type(m))
# print(isinstance(m, MyClass))
#
#'''Data Attributes'''
#
# class BankAccount:
# 	apr = 1.2
# print(BankAccount.__dict__)
# print(BankAccount.apr)
# acc_1 = BankAccount()
# acc_2 = BankAccount()
# print(acc_1 is acc_2)
# print(acc_1.__dict__, acc_2.__dict__)
# print(acc_1.apr, acc_2.apr)
# BankAccount.account_type = 'Savings'
# print(acc_1.account_type, acc_2.account_type)
# acc_1.apr = 0
# print(acc_1.__dict__, acc_2.__dict__)
# print(acc_1.apr, acc_2.apr)
# setattr(acc_2, 'apr', 10)
# print(acc_2.__dict__)
# print(getattr(acc_2, 'apr'))
# acc_3 = BankAccount
# print(getattr(acc_3, 'apr'))
# acc_1.bank = 'Acme Saving & loans'
# print(acc_1.__dict__)
# print(acc_2.__dict__)
# print(BankAccount.__dict__)
# print(type(BankAccount.__dict__))
# acc_1 = BankAccount()
# print(type(acc_1.__dict__))
# class Program:
# 	language = 'Python'
# p = Program()
# print(p.__dict__)
# p.__dict__['version'] = '3.7'
# print(p.__dict__)
# print(p.version)
# print(getattr(p, 'version'))
#
#'''Function Attributes'''
#
# class Person:
# 	def say_hello():
# 		print('Hello')
# print(Person.say_hello)
# print(type(Person.say_hello))
# Person.say_hello()
# p = Person()
# print(hex(id(p)))
# print(p.say_hello)  
#
# class Person:
# 	def say_hello(*args):
# 		print('say_hello args:', args)
# Person.say_hello()
# print(hex(id(p)))
# p.say_hello
# class Person:
# 	def set_name(instance_obj, new_name):
# 		instance_obj.name = new_name
# 		# setattr(instance_obj, 'name', new_name) 
# p = Person()
# p.set_name('Alex')
# print(p.__dict__)
# p = Person()
# Person.set_name(p, 'John')
# print(p.__dict__)
# class Person:
# 	def say_hello(self):
# 		print(f'{self} says hello')
# print(Person.say_hello, hex(id(Person.say_hello)))
# p = Person()
# print(p.say_hello) # method
# m_hello = p.say_hello
# print(m_hello)
# print(hex(id(p)))
# print(m_hello.__self__)
# class Person:
# 	def say_hello(self):
# 		print(f'isinstance method called from {self}')
# p = Person()
# print(hex(id(p)))
# print(p.say_hello)
# Person.do_work = lambda self: f'do_work called from {self}'
# print(Person.__dict__)
# print(p.say_hello)
# print(p.do_work)
# print(p.do_work())
# p.other_func = lambda *args: f'other_func called with args'
# print(p.__dict__)
# print(p.other_func())
#
#'''Initializing class instances'''
#
# class Person:
# 	def __init__(self):
# 		print(f'Initializing a new Person object: {self}')
# p = Person()
# print(hex(id(p)))
# class Person:
# 	def __init__(self, name):
# 		self.name = name
# p = Person('Eric')
# print(p.__dict__)
# class Person:
# 	def init(self, name):
# 		self.name = name
# p = Person()
# p.init('Marya')
# print(p.name)
#
#'''Creating Attributes at Run-Time'''
#
# class Person:
# 	pass
# p1 = Person()
# p2 = Person()
# p1.name = 'Alex'
# print(p1.__dict__)
# print(p2.__dict__)
# p1.say_hello = lambda: 'Hello'
# print(p1.say_hello)
# print(p1.__dict__)
# from types import MethodType
# class Person:
# 	def __init__(self, name):
# 		self.name = name
# p1 = Person("Eric")
# p2 = Person("Alex")
# print(p1.__dict__, p2.__dict__)
# def say_hello(self):
# 	return f'{self.name} says hello!'
# print(say_hello(p1))
# p1_say_hello = MethodType(say_hello, p1)
# print(p1_say_hello)
# print(p1.__dict__)
# p1.say_hello = p1_say_hello
# print(p1.__dict__)
# print(hex(id(p1)))
# print(p2.__dict__)
# print(p1.say_hello())
# print(getattr(p1, 'say_hello')())
# p1 = Person('Alex')
# print(p1.__dict__)
# p1.say_hello = MethodType(lambda self: f'{self.name} say_hello', p1)
# print(p1.say_hello())
# p1 = Person('Alex')
# p2 = Person('Eric')
# p1.say_hello = MethodType(lambda self: f'{self.name} say_hello', p2)
# print(p1.say_hello())
# print('------------------------')
# from types import MethodType
# class Person:
# 	def __init__(self, name):
# 		self.name = name
#
# 	def register_do_work(self, func):
# 		#self._do_work = MethodType(func, self)
# 		setattr(self, '_do_work', MethodType(func, self))
#
# 	def do_work(self):
# 		do_work_method = getattr(self, '_do_work', None)
#
# 		if do_work_method:
# 			return do_work_method()
# 		else:
# 			raise AttributeError('You Must first register a do_work method')
# math_teacher = Person('Eric')
# english_teacher = Person('John')
#
# def work_math(self):
# 	return f'{self.name} will teach differentials today'
#
# math_teacher.register_do_work(work_math)
# print(math_teacher.__dict__)
# print(hex(id(math_teacher)))
# print(math_teacher.do_work())
# def work_english(self):
# 	return f'{self.name} will analyze Hamlet today'
# english_teacher.register_do_work(work_english)
# print(english_teacher.__dict__)
# print(english_teacher.do_work())
# persons = [math_teacher, english_teacher]
# for p in persons:
# 	print(p.do_work())
#
#'''Properties'''
#
# class Person:
# 	def __init__(self, name):
# 		self.name = name
# p = Person('Alex')
# print(p.__dict__)
# p.name = 100
# p.name = ''
# class Person:
# 	def __init__(self, name):
# 		self.set_name(name)
#
# 	def get_name(self):
# 		return self._name
#
# 	def set_name(self, value):
# 		if isinstance(value, str) and len(value.strip()) > 0 :
# 			self._name = value.strip()
# 		else:
# 			raise ValueError('Name must be a non-empty string')
# p = Person('asd da') 
# try:
# 	Person('')
# except ValueError as ex:
# 	print(ex)
# print(p.__dict__)
# print(p.get_name())
# p.set_name('Eric')
# print(p.get_name())
# a = property()
# print(a)
# class Person:
# 	def __init__(self, name):
# 		self._name = name
#
# 	def get_name(self):
# 		print('getter called...')
# 		return self._name
#
# 	def set_name(self, value):
# 		print('setter called...')
# 		if isinstance(value, str) and len(value.strip()) > 0 :
# 			self._name = value.strip()
# 		else:
# 			raise ValueError('Name must be a non-empty string')
#
# 	name = property(fget=get_name, fset=set_name)
# p = Person('Alex')
# print(p.name)
# p.name = "Eric"
# print(getattr(p, 'name'))
# setattr(p, 'name', 'Alex')
# print(p.__dict__)
# print(p.__dict__['_name'])
# print(p._name)
# p.__dict__['name'] = 'John' 
# print(p.__dict__)
# print(getattr(p, 'name'))
#
# class Person:
# 	def __init__(self, name):
# 		self._name = name
#
# 	def get_name(self):
# 		print('getter called...')
# 		return self._name
#
# 	def set_name(self, value):
# 		print('setter called...')
# 		if isinstance(value, str) and len(value.strip()) > 0 :
# 			self._name = value.strip()
# 		else:
# 			raise ValueError('Name must be a non-empty string')
#
# 	def del_name(self):
# 		print('deleter called...')
# 		del self._name
#	
# 	name = property(fget=get_name, fset=set_name, fdel=del_name, doc="The Peron's name")
#
# p = Person('Alex')
# print(p.name)
# p.name = 'Eric'
# print(p.name)
# del p.name
# print(p.__dict__)
# print(Person.__dict__)
# #print(p.name) AttributeError: 'Person' object has no attribute '_name'
# p.name = 'Alex'
# print(p.__dict__)
# print(p.name)
# print(help(Person.name))
#
#'''Property Decorators'''
#
# p = property(lambda self: print('getting propery...'))
# print(p)
# #print(property.__dict__)
# print(p.fget)
# def my_decorator(fn):
# 	print('decorating function')
# 	def inner(*args, **kwargs):
# 		print('running decorated function')
# 		return fn(*args, **kwargs)
# 	return inner
# def undecorated_function(a, b):
# 	print('running original function')
# 	return a + b
# decorated_func = my_decorator(undecorated_function)
# print(decorated_func)
# print(decorated_func(1, 2))
# @my_decorator
# def my_func(a, b):
# 	print('running original function')
# my_func(1,2)
#
# class Person:
# 	def __init__(self, name):
# 		self._name = name
#
# 	@property
# 	def name(self):
# 		print('getter called...')
# 		return self._name
#
# p = Person("John")
# print(p.name)
# print(property.__dict__)
#
# def get_prop(self):
# 	return 'getter called...'
#
# def set_prop(self, value):
# 	return 'setter called...'
#
# def del_prop(self):
# 	return 'deleter called...'
# p = property(get_prop)
# print(p.fget)
# p1 = p.setter(set_prop)
# print(p1 is p)
# print(p.fget is p1.fget)
# print(p1.fset)
# p = property(get_prop)
# p = p.setter(set_prop)
# class Person:
# 	name = p
# person = Person()
# print(person.name)
# person = Person()
# def name(self):
# 	print('getter...')
# print(hex(id(name)))
# name = property(name)
# print(type(name), hex(id(name)), hex(id(name.fget)))
# name_temp = name
# def name(self, value):
# 	print('setter...')
# print(type(name), hex(id(name)))
# name = property(name)
#
#'''Read-only computed properties
#
# from math import pi
#
# class Circle:
# 	def __init__(self, radius):
# 		self.radius = radius
#
# 	@property
# 	def area(self):
# 		print('calculating area...')
# 		return pi * (self.radius ** 2)
#
# 	def area_1(self):
# 		print('calculating area...')
# 		return pi * (self.radius ** 2)
#
# c = Circle(1)
# print(c.area)
# print(c.area_1())
#
# class Circle:
# 	def __init__(self, radius):
# 		self._radius = radius
# 		self._area = None
#
# 	@property
# 	def radius(self):
# 		return self._radius
#
# 	@radius.setter
# 	def radius(self, value):
# 		self._area = None
# 		self._radius = value
#
# 	@property
# 	def area(self):
# 		if self._area is None:
# 			print('Calculating area...')
# 			self._area = pi * (self.radius ** 2)
# 		return self._area
# c = Circle(1)
# print(c.area)
# c.radius = 2
# print(c.__dict__)
# print(c.area)
# import urllib
# from time import perf_counter
#
# class WebPage:
# 	def __init__(self, url):
# 		self.url = url
# 		self._page = None
# 		self._load_time_secs = None
# 		self._page_size = None
#
# 	@property
# 	def url(self):
# 		return self._url
#	
# 	@url.setter
# 	def url(self, value):
# 		self._url = value
# 		self._page = None
#
# 	@property
# 	def page(self):
# 		if self._page is None:
# 			self.download_page()
# 		return self._page
#
# 	@property
# 	def page_size(self):
# 		if self._page is None:
# 			self.download_page()
# 		return self._page_size
#	
# 	@property
# 	def time_elapsed(self):
# 		if self._page is None:
# 			self.download_page()
# 		return self._load_time_secs
#
# 	def download_page(self):
# 		self._page_size = None
# 		self._load_time_secs = None
# 		start_time = perf_counter()
# 		with urllib.request.urlopen(self.url) as f:
# 			self._page = f.read()
# 		end_time = perf_counter()
# 		self._page_size = len(self._page)
# 		self._load_time_secs = end_time - start_time
#
# urls = [
# 	'https://www.google.com',
# 	'https://www.python.org',
# 	'https://www.yahoo.com'
# ]
# for url in urls:
# 	page = WebPage(url)
# 	print(f'{url}\tsize={format(page.page_size, "_")}\telapsed={page.time_elapsed:.2f} secs') 
#
#'''Deleting Properties'''
#
# print('Without decorators\n-----------------')
# class Person:
# 	def __init__(self, name):
# 		self.name = name
#
# 	def get_name(self):
# 		print('getter...')
# 		return self._name
#
# 	def set_name(self, value):
# 		print("setter...")
# 		self._name = value
#
# 	def del_name(self):
# 		print('deleter...')
# 		del self._name
#
# 	name = property(fget=get_name, fset=set_name, fdel=del_name, doc='Person name')
#
# p = Person("Guido")
# print(p.name)
# print(p.__dict__)
# delattr(p, 'name')
# print(p.__dict__)
# print(Person.__dict__)
# p.name = ('Alex')
# print(p.__dict__)
# print('--------------------\nWith decorators\n-----------------')
# class Person:
# 	def __init__(self, name):
# 		self.name = name
#
# 	@property
# 	def name(self):
# 		'''Person Name'''
# 		print('getter...')
# 		return self._name
#
# 	@name.setter
# 	def name(self, value):
# 		print("setter...")
# 		self._name = value
#
# 	@name.deleter
# 	def name(self):
# 		print('deleter...')
# 		del self._name
#
# p = Person("Alex")
# print(p.__dict__)
# del p.name
# print(p.__dict__)
# p.name = 'Guido'
# print(p.__dict__)
# class Person:
# 	def hello(arg='default'):
# 		print(f'Hello, with arg={arg}')
# Person.hello(100)
# p = Person()
# p.hello()
# class MyClass:
# 	def hello():
# 		print('hello...')
#
# 	def instance_hello(arg):
# 		print(f'hello from {arg}')
#
# 	@classmethod
# 	def class_hello(arg):
# 		print(f'hello from {arg}')
#
# 	@staticmethod
# 	def static_hello():
# 		print('Static method called')
#
# m = MyClass()
# MyClass.hello()
# m.instance_hello()
# m.class_hello()
# MyClass.class_hello()
# print(MyClass.class_hello)
# print(MyClass.instance_hello)
# print(m.class_hello)
# MyClass.static_hello()
# m.static_hello()
# print(m.static_hello)
# from datetime import datetime, timezone, timedelta
# class Timer:
# 	tz = timezone.utc
#
# 	@classmethod
# 	def set_tz(cls, offset, name):
# 		cls.tz = timezone(timedelta(hours=offset), name)
#
# Timer.set_tz(-7, 'MST')
# print(Timer.tz)
# t1 = Timer()
# t2 = Timer()
# print(t1.tz, t2.tz)
# Timer.set_tz(-8, 'PST')
# print(t1.tz, t2.tz)
#
# class Timer:
# 	tz = timezone.utc
#
# 	@classmethod
# 	def set_tz(cls, offset, name):
# 		cls.tz = timezone(timedelta(hours=offset), name)
#
# 	@staticmethod
# 	def current_dt_utc():
# 		return datetime.now(timezone.utc)
#
# t = Timer()
# print(t.current_dt_utc())
# print(Timer.current_dt_utc())
#
# class Timer:
# 	tz = timezone.utc
#
# 	@classmethod
# 	def set_tz(cls, offset, name):
# 		cls.tz = timezone(timedelta(hours=offset), name)
#
# 	@staticmethod
# 	def current_dt_utc():
# 		return datetime.now(timezone.utc)
#
# 	@classmethod
# 	def current_dt(cls):
# 		return datetime.now(cls.tz)
#
# print(Timer.current_dt_utc(), Timer.current_dt())
# t1 = Timer()
# t2 = Timer()
# print(t1.current_dt_utc(), t1.current_dt())
# t2.set_tz(-7, 'MST')
# print(t1.tz, t2.tz)
# print(t1.__dict__, t2.__dict__)
# print(t1.current_dt(), t2.current_dt())
# print(t1.current_dt_utc(), t1.current_dt(), t2.current_dt())
#
# from datetime import datetime, timezone, timedelta
#
# class TimerError(Exception):
# 	'''A Custom Exception used for Timer Class'''
#
# class Timer:
# 	tz = timezone.utc
#
# 	@classmethod
# 	def set_tz(cls, offset, name):
# 		cls.tz = timezone(timedelta(hours=offset), name)
#
# 	@staticmethod
# 	def current_dt_utc():
# 		return datetime.now(timezone.utc)
#
# 	@classmethod
# 	def current_dt(cls):
# 		return datetime.now(cls.tz)
#
# 	def start(self):
# 		self._time_start = self.current_dt_utc()
# 		self._time_end = None
#
# 	def stop(self):
# 		if self._time_start is None:
# 			raise TimerError('Timer Must be started before it can be stopped')
# 		self._time_end = self.current_dt_utc()
#
# 	@property
# 	def start_time(self):
# 		if self._time_start is None:
# 			raise TimerError('Timer has not been started')
# 		return self._time_start.astimezone(self.tz)
#	
# 	@property
# 	def end_time(self):
# 		if self._time_end is None:
# 			raise TimerError("Timer has not been Started")
# 		return self._time_end.astimezone(self.tz)
#		
# 	@property
# 	def elapsed(self):
# 		if self._time_start is None:
# 			raise TimerError("Time must be started before an elapsed time can be calculated")
# 		if self._time_end is None:
# 			elapsed_time = self.current_dt_utc() - self._time_start
# 		else:
# 			elapsed_time = self._time_end - self._time_start
# 		return elapsed_time.total_seconds()
#
# from time import sleep
#
# t1 = Timer()
# t1.start()
# sleep(2)
# t1.stop()
# print(f'Start Time: {t1.start_time}')
# print(f'End Time: {t1.end_time}')
# print(f'Elapsed Time: {t1.elapsed}')
# t2 = Timer()
# t2.start()
# sleep(3)
# t2.stop()
# print(f'Start Time: {t2.start_time}')
# print(f'End Time: {t2.end_time}')
# print(f'Elapsed Time: {t2.elapsed}') 
#
#'''Class Body Scope'''
#
class Language:
	MAJOR = 3
	MINOR = 7
	REVISION = 4
	FULL = f'{MAJOR}.{MINOR}.{REVISION}'
print(Language.FULL)
print('------------\nProperty static and class methods together.')
class Language:
	MAJOR = 3
	MINOR = 7
	REVISION = 4

	@property
	def version(self):
		return f'{self.MAJOR}.{self.MINOR}.{self.REVISION}'

	@classmethod
	def cls_version(cls):
		return f'{cls.MAJOR}.{cls.MINOR}.{cls.REVISION}'

	@staticmethod
	def static_version():
		return f'{Language.MAJOR}.{Language.MINOR}.{Language.REVISION}'

l= Language()
print(l.version)
print(Language.cls_version())
print(Language.static_version())
class Language:
	MAJOR = 3
	MINOR = 7
	REVISION = 4

def full_version():
	return f'{Language.MAJOR}.{Language.MINOR}.{Language.REVISION}'
print(full_version())
class Language:
	MAJOR = 3
	MINOR = 7
	REVISION = 4

	version = full_version
print(Language.version())


class Language:
	MAJOR = 3
	MINOR = 7
	REVISION = 4

	def version(self):
		return f'{MAJOR}.{MINOR}.{REVISION}'	

MAJOR = 0
MINOR = 0
REVISION = 1

def gen_class():
	MAJOR = 0
	MINOR = 4
	REVISION = 2

	class Language:
		MAJOR = 3
		MINOR = 8
		REVISION = 6

		@classmethod
		def version(cls):
			return f'{MAJOR}.{MINOR}.{REVISION}'
	return Language

cls = gen_class()
print(cls.version())
import inspect
print(inspect.getclosurevars(cls.version))
name = 'Guido'

class MyClass:
	name = 'Raymond'
	list_1 = [name] * 3
	list_2 = [name for i in range(3)]

	@classmethod
	def hello(cls):
		return '{} says hello'.format(name)
print(MyClass.hello())
print(MyClass.list_1)
print(MyClass.list_2)