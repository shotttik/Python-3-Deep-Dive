#'''Integer Data Types'''
# print(type(100))
# import sys
# print(sys.getsizeof(0))
# print(sys.getsizeof(2**1000))
#
# import time
# def calc(a):
# 	for i in range(10000000):
# 		a * 2
# start = time.perf_counter()
# calc(10)
# end = time.perf_counter()
# print(end - start)
# start = time.perf_counter()
# calc(2*100)
# end = time.perf_counter()
# print(end - start)
# start = time.perf_counter()
# calc(2**10000)
# end = time.perf_counter()
# print(end - start)
#
#'''INTEGERS OPERATIONS'''
#
# print(type(1+1))
# print(type(2 * 3))
# print(type(4 - 10))
# print(type(3 ** 6))
# print(type(2 / 3))
# print(type(10 / 2))
# print(10 / 2)
# import math
# print(math.floor(3.15))
# print(math.floor(3.99999))
# print(math.floor(-3.14))
# print(math.floor(-3.00000001))
# print(math.floor(-3.000000000001))
# print(math.floor(-3.0000000000000001))
#import math
# a = 33
# b = 16
# print(a / b)
# print(a // b)
# print(math.floor(a / b))
# a = -33
# b = 16
# print(a / b)
# print(a // b)
# print(math.floor(a / b))
# a = -33
# b = 16
# print(a / b)
# print(a // b)
# print(math.floor(a / b))
# print(math.trunc(a/b))
# a = b * (a // b) + (a % b)
# print('------------------')
# a = 13
# b = 4
# print(f'{a}/{b}={a/b}')
# print(f'{a}//{b}={a//b}')
# print(f'{a}%{b}={a%b}')
# print( a == b * (a//b) + (a%b))
# print('------------------')
# a = -13
# b = 4
# print(f'{a}/{b}={a/b}')
# print(f'{a}//{b}={a//b}')
# print(f'{a}%{b}={a%b}')
# print( a == b * (a//b) + (a%b))
# print('------------------')
# a = 13
# b = -4
# print(f'{a}/{b}={a/b}')
# print(f'{a}//{b}={a//b}')
# print(f'{a}%{b}={a%b}')
# print( a == b * (a//b) + (a%b))
# print('------------------')
# a = -13
# b = -
# 4
# print(f'{a}/{b}={a/b}')
# print(f'{a}//{b}={a//b}')
# print(f'{a}%{b}={a%b}')
# print( a == b * (a//b) + (a%b))
# print('------------------')
#
#'''INTEGERS CONSTRUCTORS AND BASES
# print(type(10))
# print(int(10.5))
# print(int(True))
# print(int(False))
# import fractions
# a = fractions.Fraction(22, 7)
# print(a)
# print(float(a))
# print(int(a))
# print(int("12345"))
# print(int('101', 2))
# print(int('FF', 16))
# print(int('ff', 16))
# print(int("A ", 11))
# print(bin(10))
# print(oct(10))
# print(hex(255))
# a = int('101', 2)
# b = 0b101
# print(a)
# print(b)
#
# def from_base10(n, b):
# 	if n < 2:
# 		raise ValueError('Base b must be >= 2')
# 	if n < 0:
# 		raise ValueError('Number n must be >= 0')
# 	if n == 0:
# 		return [0]
# 	digits = []
# 	while n > 0:
# 		# m, n = n % b, n // b # equal to down
# 		n, m = divmod(n, b) 
# 		digits.insert(0, m)
# 	return digits
# print(from_base10(10, 2))
# print(from_base10(255, 16))
#
# def encode(digits, digit_map):
# 	if max(digits) >= len(digit_map):
# 		raise ValueError("digit_map is not long enough to encode the digits")
# 	# encoding = ''	
# 	# for d in digits:
# 	# 	encoding += digit_map[d]
# 	# return encoding
# 	return ''.join([digit_map[d] for d in digits])
# print(encode([15, 15], '0123456789ABCDEF'))
#
# def rebase_from10(number, base):
# 	digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 	if base < 2 or base > 36:
# 		raise ValueError('Invalid base: 2 <= base <= 36')
# 	sign = -1 if number < 0 else 1
# 	# equal to top
# 	# if number < 0:
# 	# 	sign = -1
# 	# else:
# 	# 	sign = 1
# 	number *= sign
#
# 	digits = from_base10(number, base)
# 	encoding = encode(digits, digit_map)
# 	if sign == -1:
# 		encoding = '-' + encoding
# 	return encoding
# e = rebase_from10(10, 2)
# print(e)
# print(int(e, base=2))
# e = rebase_from10(3451, 16)
# print(e)
# print(int(e, base=16))
#
#'''Rational Numbers'''
#
# from fractions import Fraction
# print(Fraction(1))
# print(Fraction(denominator=1, numerator=2))
# print(Fraction(1, 2))
# print(Fraction(numerator=1, denominator=2))
# print(Fraction(0.125))
# print(Fraction('0.125'))
# print(Fraction('22/7'))
# x = Fraction(2, 3)
# y = Fraction(3, 4)
# print(x + y)
# print(x * y)
# print(x / y)
# print(Fraction(8, 16))
# print(Fraction(1, -4))
# x = Fraction(1, -4)
# print(x.numerator)
# print(x.denominator)
# from fractions import Fraction
# import math
# x = Fraction(math.pi)
# print(x)
# print(float(x))
# y = Fraction(math.sqrt(2))
# print(y)
# print(float(y))
# a = 0.125
# print(a)
# b = 0.3
# print(b)
# print(Fraction(a))
# print(Fraction(b))
# print(format(b, '0.5f'))
# print(format(b, '0.15f'))
# print(format(b, '0.25f'))
# print(Fraction(b))
# x = Fraction(0.3)
# print(x.limit_denominator(10))
# x = Fraction(math.pi)
# print(x)
# print(float(x))
# print(x.limit_denominator(10))
# print(22/7)
# print(x.limit_denominator(100000))
# print(312689/99532)
#
#'''FLOATS Internal Representation'''
# print(float(10))
# print(float(10.4))
# print(float('12.5'))
# from fractions import Fraction
# a = Fraction('22/7')
# print(float(a))
# print(0.1)
# print(format(0.1, '.15f'))
# print(format(0.1, '.25f'))
# print(0.125)
# print(1/8)
# print(format(0.125, '.25f'))
# print('----------------------------')
# a = 0.1 + 0.1 + 0.1
# b = 0.3
# print(a == b)
# print(format(a, '.25f'))
# print(format(b, '.25f'))
#
#'''Floats equality testing'''
#
# x = 0.1
# print(format(x, '.25f'))
# print(x)
# x = 0.125
# print(x)
# print(format(x, '.25f'))
# x = 0.125 + 0.125 + 0.125
# y = 0.375
# print(x == y)
# x = 0.1 + 0.1 + 0.1
# y = 0.3
# print(x == y)
# print(format(x, '.25f'))
# print(format(y, '.25f'))
#
# print(round(x, 3) == round(y, 3))
# x = 10000.01
# y = 10000.02
# print(y/x)
#
# x = 0.01
# y = 0.01
# print(y/x)
# print(round(x, 1) == round(y, 1))
#
# x = 10000.01
# y = 10000.02
# print(round(x, 1) == round(y, 1))
#
# from math import isclose
# help(isclose)
#
# x = 0.1 + 0.1 + 0.1
# y = 0.3
# print(isclose(x, y))
#
# x = 123456789.01
# y = 123456789.02
# print(isclose(x, y, rel_tol=0.01 ))
#
# x = 0.01
# y = 0.02
# print(isclose(x, y, rel_tol=0.01))
#
# x = 0.000001
# y = 0.000002
# print(isclose(x, y, rel_tol=0.01))
# print(isclose(x, y, abs_tol=0.01))
#
# x = 0.0000001
# y = 0.0000002
# a = 123456789.01
# b = 123456789.02
#
# print(isclose(x, y, abs_tol=0.0001, rel_tol=0.01))
# print(isclose(a, b, abs_tol=0.0001, rel_tol=0.01))
#
#'''Floats Coercing to Integers'''
#
# from math import trunc
# help(trunc)
# print(trunc(10.3), trunc(10.5), trunc(10.9))
# print(int(10.4), int(10.5), int(10.9))
# from math import floor
# help(floor)
# print(floor(10.3), floor(10.5), floor(10.9))
# print(trunc(-10.4), trunc(-10.5), trunc(-10.9))
# print(floor(-10.4), floor(-10.5), floor(-10.9))
# from math import ceil
# help(ceil)
# print(ceil(10.4), ceil(10.5), ceil(10.9))
# print(ceil(-10.4), ceil(-10.5), ceil(-10.9))
#
#'''Floats Rounding'''
#
# help(round)
# a = round(1.9)
# print(a, type(a))
# a = round(1.9, 0)
# print(a, type(a))
# print(round(1.8888, 3), round(1.8888, 2), round(1.8888, 0))
# print(round(888.88, 1), round(888.88, 0), round(888.88, -1), round(888.88, -4))
# print(round(800, -4))
# print(round(1.25, 1))
# print(round(1.35, 1))
# print(round(-1.25, 1), round(-1.35, 1))
# def _round(x):
# 	from math import copysign
# 	return int(x + 0.5 * copysign(1, x))
# print(_round(1.5))
# print(round(2.5), _round(2.5))
#
#'''Decimals'''
#
# import decimal
# from decimal import Decimal
# print(decimal.getcontext())
# print(decimal.getcontext().rounding)
# decimal.getcontext().prec = 6
# print(decimal.getcontext())
# g_ctx = decimal.getcontext()
# print(type(g_ctx))
# g_ctx.rounding = 'ROUND_HALF_UP'
# g_ctx.prec = 28
# g_ctx.rounding = 'ROUND_HALF_EVEN'
# print(decimal.getcontext())
# print(type(decimal.localcontext()))
# print(type(decimal.getcontext()))
# x = Decimal('1.25')
# y = Decimal('1.35')
# with decimal.localcontext() as ctx:
# 	ctx.prec = 6
# 	ctx.rounding = decimal.ROUND_HALF_UP
# 	print(ctx)
# 	print(decimal.getcontext())
# 	print(id(ctx) == id(decimal.getcontext()))
# 	print(round(x, 1))
# 	print(round(y, 1))
# print(round(x, 1))
# print(round(y, 1))
#
#'''Decimals Constructors and Contexts
#
# import decimal
# from decimal import Decimal
# print(Decimal(10))
# print(Decimal(-10))
# print(Decimal('10.1'))
# print(Decimal('-10.2423'))
# print(Decimal((0, (3,1,4,1,5), -4)))
# print(Decimal((1, (3,1,4,1,5), -4)))
# print(format(0.1, '.25f'))
# print(Decimal(0.1))
# print(Decimal('0.1'))
# print(Decimal(0.1) == Decimal('0.1'))
# print(Decimal(10) == Decimal('10'))
# print(decimal.getcontext())
# decimal.getcontext().prec = 2
# a = Decimal('0.12345')
# b = Decimal('0.12345')
# print(a, b)
# print(0.12345 + 0.12345)
# print(a + b)
#
# decimal.getcontext().prec = 6
# a = Decimal('0.12345')
# b = Decimal('0.12345')
# print(a + b)
# with decimal.localcontext() as ctx:
# 	ctx.prec = 2
# 	c = a + b
# 	print(f'c within local context: {c}')
# print(f'c within local context: {c}')
#
#'''Decimals Mathematical operations'''
#
# import decimal
# from decimal import Decimal
# # // and %
# # n = d * (n//d) + (n%d)
# x = -10
# y = 3
# print(x // y, x % y)
# print(divmod(x, y))
# print(x == y * (x // y) + (x % y))
#
# x = Decimal(10)
# y = Decimal(3)
# print(x // y, x % y)
# print(divmod(x, y))
# print(x == y * (x // y) + (x % y))
# # Other math functions
# a = Decimal('1.5')
# print(a.ln())
# print(a.exp())
# print(a.sqrt())
# import math
# print(math.sqrt(a))
# x = 2
# x_dec = Decimal(2)
# root_float = math.sqrt(x)
# root_mixed = math.sqrt(x_dec)
# root_dec = x_dec.sqrt()
# print(format(root_float, '1.27f'))
# print(format(root_mixed, '1.27f'))
# print(format(root_dec, '1.27f'))
# print(format(root_float * root_float, '1.27f'))
# print(format(root_mixed * root_mixed, '1.27f'))
# print(format(root_dec * root_dec, '1.27f'))
#
# Decimals Performance Considerations
# 
# from decimal import Decimal
# import sys
# a = 3.1415
# b = Decimal('3.1415')
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# import time
#
# def run_float(n=1):
# 	for i in range(n):
# 		a = 3.1415
#
# def run_decimal(n=1):
# 	for i in range(n):
# 		a = Decimal('3.1415')
# n = 10000000
# start = time.perf_counter()
# run_float(n)
# end = time.perf_counter()
# print('float:', end-start)
# start = time.perf_counter()
# run_decimal(n)
# end = time.perf_counter()
# print('decimal:', end-start)
#
# import math
# n = 5000000
#
# def run_float(n=1):
# 	a = 3.1415
# 	for i in range(n):
# 		math.sqrt(a)
#
# def run_decimal(n=1):
# 	a = Decimal('3.1415')
# 	for i in range(n):
# 		a.sqrt()
#
# start = time.perf_counter()
# run_float(n)
# end = time.perf_counter()
# print('float:', end-start)
# start = time.perf_counter()
# run_decimal(n)
# end = time.perf_counter()
# print('decimal:', end-start)
#
#'''Complex Numbers'''
#
#help(complex)
# a = complex(1, 2)
# b = 1 + 2j
# print(a == b)
# print(a.real, type(a.real))
# print(a.imag, type(a.imag))
# print(a.conjugate())
# a = 1 + 2j
# b = 10 + 8j
# print(a + b)
# print(a * b)
# print(a / b)
# a = 0.1j
# print(format(a.imag, '.25f'))
# print(a + a + a == 0.3j)
# print(format((a + a + a).imag, '.25f'))
# print(format((0.3j).imag, '.25f'))
# import math
# print(math.sqrt(2))
# print(math.pi)
# import cmath
# print(cmath.pi)
# print(type(cmath.pi))
# a = 1 + 2j
# #print(math.sqrt(a)) Typeerror: can't convert complex to float. 
# print(cmath.sqrt(a))
# a = 1 + 1j
# print(cmath.phase(a))
# print(cmath.pi/4)
# print(abs(a))
# print(cmath.rect(math.sqrt(2), math.pi/4))
# RHS = cmath.exp(cmath.pi * 1j) + 1
# print(RHS)
# print(cmath.isclose(RHS, 0))
# print(cmath.isclose(RHS, 0, abs_tol=0.0001))
#
#'''Booleans'''
#
# print(type(True), id(True), int(True))
# print(type(False), id(False), int(False))
# print(3 < 4)
# print(type(3 < 4))
# print(id(3 < 4))
# print((3 < 4) is True) 
# print((1 == 2) == False)
# print(1 == 2 == False) # print(1 == 2 and 2 == False)
# print(int(True), int(False))
# print(1 + True)
# print(100 * False)
# print(True > False)
# print((True + True + True) % 2)
# print(-True)
# print(bool(0))
# print(bool(1))
# print(int(True))
# print(bool(True))
# print(bool(False))
# print(bool(100))
# print(bool(-1))
# print(bool(0))
#
#'''Booleans Truth values'''
#
#only 0 is False
# print(bool(1))
# print(bool(0))
# print(bool(-1))
# print(bool(100))
# print(bool())
# print(bool(0), 0 != 0)
# print(bool(100), (100).__bool__())
# print(bool(0), (0).__bool__())
# a = []
# print(bool(a))
# print(a.__len__())
# print(bool(a))
# print(bool(a.__len__()))
# print(bool(0.0), bool(0+0j))
# from decimal import Decimal
# from fractions import Fraction
# print(bool(Fraction(0, 1)), bool(Decimal('0.0')))
# print(bool(10.5), bool(1j), bool(Fraction(1, 2)), bool(Decimal('10.5')))
#
# a = [1, 2]
# b = 'abc'
# c = (1, 2)
# print(bool(a), bool(b), bool(c))
#
# a = {'a': 1}
# b = {1, 2}
# print(a, b)
# print(bool(a), bool(b))
# print(bool(None))
#
# a = [1, 2, 3]
# if a is not None and len(a) > 0:
# 	print(a[0])
# else:
# 	print('nothing to see here...')
#
# a = []
# if a:
# 	print(a[0])
# else:
# 	print('nothing to see here...')
#
#'''Booleans: Precedence and Shorting-Circuting'''
#
# a = 10
# b = 2
#
# if a/b > 2:
# 	print('a is at least twice b')
#
# a = 10
# b = None
#
# if b and  a/b > 2:
# 	print('a is at least twice b')
#
# import string
# #help(string)
# a = 'c'
# print(a in string.ascii_uppercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.ascii_letters)
# name = ''
# if name and name[0] in string.digits:
# 	print("Name cannot stat with a digit")
# name = 'abc'
# print(bool(name))
#
#'''Booleans: Boolean Operators'''
#
# s1 = None
# s2 = ''
# s3 = 'abc'
# 
# s1 = s1 or 'n/a'
# s2 = s2 or 'n/a'
# s3 = s3 or 'n/a'
#
# print(s1, s2, s3)
#
# s1 = None
# s2 = ''
# s3 = 'abc'
#
# print((s1 and s1[0]) or 'n/a')
# print((s2 and s2[0]) or 'n/a')
# print((s3 and s3[0]) or 'n/a')
#
# print(bool('abc'))
# print(bool(''))
#
#'''Comprasion Operators'''
#
# print(0.1 is (3+4j))
# print(3 is 3)
# 'a' in 'this is a test'
# print(3 not in [1, 2, 3])
# print('key1' in {'key1': 1})
# print(1 in {'key1': 1})
# print(1 + 1j < 3 + 4j) TypeError: '<' not supported between instances of 'complex' and 'complex'
# from decimal import Decimal
# from fractions import Fraction
# print(4 < Decimal('10.5'))
# print(Fraction(2, 3) < Decimal('0.5'))
# print(4 == 4 + 0j)
# print(True == Fraction(2, 2))
# print(True < Fraction(3, 2))
# print((1 < 2 < 3) == (1 < 2 and 2 < 3))
# print(3 < 2 < 1/0)
# print(3 < 2 and 2 < 1/0)
# # print(3 < 4 < 1/0) ZeroDivisionError: division by zero
# print(1 < 2 > -5)
# print(1 < 2 > -5 == Decimal('-5.0'))
# import string
# print('A' < 'a' < 'z' > 'Z' in string.ascii_letters)
