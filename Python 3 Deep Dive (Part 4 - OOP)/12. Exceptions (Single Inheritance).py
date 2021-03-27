# '''Python Exceptions'''

# print(type(BaseException), type(Exception))

# ex = Exception()

# print(ex.__class__)
# print(isinstance(ex, Exception))
# print(isinstance(ex, BaseException))
# print(issubclass(IndexError, LookupError))
# print(issubclass(IndexError, Exception))
# l = [1, 2, 3, 4]
# #l[4] IndexError: list index out of range
# try:
# 	l[4]
# except IndexError as ex:
# 	print(ex.__class__, ':', str(ex))

# try:
# 	l[4]
# except LookupError as ex:
# 	print(ex.__class__, ':', str(ex))	

# try:
# 	l[4]
# except Exception as ex: #do not try this at home
# 	print(ex.__class__, ':', str(ex))	

# ex = ValueError('custom message')

# print(hasattr(BaseException, '__repr__'))
# print(str(ex), ':',repr(ex))

# def func_1():
# 	func_2()

# def func_2():
# 	try:
# 		func_3()
# 	except ValueError:
# 		print('Eror occured - silencing it')

# def func_3():
# 	ex = ValueError('Some custom message')
# 	raise ex

# print(func_1())

# def square(seq, index):
# 	return seq[index] ** 2

# def square(seq, max_n):
# 	for i in range(max_n):
# 		try:
# 			yield square(seq, i)
# 		except Exception:
# 			return

# l = [1, 2, 3]
# print(list(square(l, 4)))
#
#'''Handling exceptions'''
#
# try:
# 	raise ValueError('custom message', 'secondary message')
# except ValueError as ex:
# 	print(repr(ex))

# def func_1():
# 	raise IndexError('bad value')

# try:
# 	func_1()
# except ValueError as ex:
# 	print("Handling a value error", repr(ex))
# except IndexError as ex:
# 	print('Handling an index error', repr(ex))


# try:
# 	raise ValueError()
# except ValueError:
# 	print('value error')
# else:
# 	print('no except')

# try:
# 	pass
# except ValueError:
# 	print('value error')
# else:
# 	print('No exception')

# try: 
# 	raise ValueError
# except ValueError:
# 	print('ValueError')
# print('no exception')

# def convert_int(val):
# 	if not isinstance(val, int):
# 		raise TypeError()
# 	if val not in {0, 1}:
# 		raise ValueError('Integer values 0 or 1 only')
# 	return bool(val)

# def convert_str(val):
# 	if not isinstance(val, str):
# 		raise TypeError()

# 	val = val.casefold()
# 	if val in {'0', 'f', 'false'}:
# 		return False
# 	elif val in {'1', 't', 'true'}:
# 		return True
# 	else:
# 		raise ValueError('Admissible string values are: T, F, True, False, 0, 1')

# class ConversionError(Exception):
# 	pass

# def make_bool(val):
# 	try:
# 		try:
# 			b = convert_int(val)
# 		except TypeError:
# 			try:
# 				b = convert_str(val)
# 			except TypeError:
# 				raise ConversionError(f'the type is inadmissible...')
# 	except ValueError as ex:
# 		raise ConversionError(f'The value {val} cannot be converted to a bool: {ex}')
# 	else:
# 		return b


# values = [True, 0, 'T', 'false', 10, 'ABC', 1.0]
# for value in values:
# 	try:
# 		result = make_bool(value)
# 	except ConversionError as ex:
# 		result = str(ex)

# 	print(value, result)


# def make_bool(val):
# 	if isinstance(val, int):
# 		if val in {0, 1}:
# 			return bool(val)
# 		else:
# 			raise ConversionError('Invalid Integer Value')
# 	if isinstance(val, str):
# 		if val.casefold() in {'1', 'true', 't'}:
# 			return True
# 		if val.casefold() in {'0', 'false', 'f'}:
# 			return False
# 		raise ConversionError('Invalid string Value')
# 	raise ConversionError('Invalid Type')	

# values = [True, 0, 'T', 'false', 10, 'ABC', 1.0]
# for value in values:
# 	try:
# 		result = make_bool(value)
# 	except ConversionError as ex:
# 		result = str(ex)

# 	print(value, result)


# def get_item_forgive_me(seq, idx, default=None):
# 	try: 
# 		return seq[idx]
# 	except (IndexError, TypeError, KeyError):
# 		return default

# def get_item_ask_perm(seq, idx, default=None):
# 	if hasattr(seq, '__getitem__'):
# 		if idx < len(seq):
# 			return seq[idx]
# 	return default

# print(get_item_forgive_me([1, 2, 3], 10, 'nope'))
# print(get_item_ask_perm([1, 2, 3], 10, 'nope'))
# print(get_item_forgive_me({'a': 100}, 'a'))
# try:
# 	print(get_item_ask_perm({'a': 100} , 'a'))
# except TypeError as ex:
# 	print(ex)

# def get_item_ask_perm(seq, idx, default=None):
# 	if hasattr(seq, '__getitem__'):
# 		if isinstance(seq, dict):
# 			return seq.get(idx, default)
# 		elif isinstance(idx, int):
# 			if idx < len(seq):
# 				return seq(idx)
# 		if idx < len(seq):
# 			return seq[idx]
# 	return default

# try:
# 	print(get_item_ask_perm({'a': 100} , 'a'))
# except TypeError as ex:
# 	print(ex)
#
#'''Raising Exceptions'''
#
# class Person(object):
# 	pass

# try:
# 	raise Person()
# except TypeError as ex:
# 	print(ex)

# ex = BaseException('a', 'b', 'c')
# print(ex.args)
# print(str(ex))
# print(repr(ex))

# ex = ValueError('a', 'b', 'c')
# print(ex.args)
# print(str(ex))
# print(repr(ex))
# try:
# 	raise ValueError('some message...', 100, 200)
# except ValueError as ex:
# 	print(ex.args)

# def div(a, b):
# 	try:
# 		return a // b
# 	except ZeroDivisionError as ex:
# 		print('loggin exception...', repr(ex))
# 		raise
# div(1, 0)


# class CustomError(Exception):
# 	"""docstring for Custom Exception"""

# def my_func(a, b):
# 	try:
# 		return a // b
# 	except ZeroDivisionError as ex:
# 		print('loggin exception...', repr(ex))
# 		raise CustomError(*ex.args)
# my_func(1, 0)

# try:
# 	raise ValueError('level 1')
# except ValueError:
# 	try:
# 		raise TypeError('Level 2')
# 	except TypeError:
# 		raise KeyError('Level 3')
#
#
#'''Custom Exception'''
#
#
# class TimeoutError(Exception):
# 	"""Timeout Exception"""

# import sys

# try:
# 	raise TimeoutError('timeout occured')
# except:
# 	ex_type, ex, tb = sys.exc_info()
# 	print(ex_type, ex, tb)  #ex.__traceback__


# class ReadOnlyError(AttributeError):
# 	"""Indicates an attribute is read-only"""

# try:
# 	raise ReadOnlyError('Account number is read-only', 'BA10001')
# except ReadOnlyError as ex:
# 	print(repr(ex))

# try:
# 	raise ReadOnlyError('Account number is read-only', 'BA10001')
# except AttributeError as ex:
# 	print(repr(ex))

# class WebScraperException(Exception):
# 	"""BASE exception for WebScraper"""


# class HTTPException(WebScraperException):
# 	"""General HTTP exception for WebScraper"""


# class InvalidUrlException(HTTPException):
# 	"""Indicates the url is invalid (dnslookup fail)"""


# class TimeoutException(HTTPException):
# 	"""Indicates a general timeout exception in htttp connectivity"""


# class PingTimeoutException(TimeoutException):
# 	"""Ping time out"""


# class LoadTimeoutException(TimeoutException):
# 	"""Page load Time out"""


# class ParserException(WebScraperException):
# 	"""General page parsing exception"""

# try:
# 	raise PingTimeoutException("PING to www. Timed out")
# except HTTPException as ex:
# 	print(repr(ex)) 

# try:
# 	raise PingTimeoutException("PING to www. Timed out")
# except WebScraperException as ex:
# 	print(repr(ex)) 
