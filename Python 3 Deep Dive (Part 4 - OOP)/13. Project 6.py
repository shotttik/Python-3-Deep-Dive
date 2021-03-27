from datetime import datetime

class WidgetException(Exception):
	message = 'Generic Widget exception.'

	def __init__(self, *args, customer_message=None):
		super().__init__(args)
		if args:
			self.message = args[0]
		self.customer_message = customer_message if customer_message is not None else self.message

	def log_exception(self):
		exception = {
			'type': type(self).__name__,
			'message': self.message,
			'args': self.args[1:]
		}
		print(f'EXCEPTION: {datetime.now().isoformat()}: {exception}')

# ex1 = WidgetException('some custom message', 10, 100)
# ex2 = WidgetException(customer_message='A custom user message.')
# print(ex1.args)
# print(ex2.args)
# ex1.log_exception()
# ex2.log_exception()


class SupplierException(WidgetException):
	message = 'Supplier exception'

class NotManufacturedException(SupplierException):
	message = 'Widget is no longer manufactured by Supplier'

class ProductionDelayedException(SupplierException):
	message = 'Widget production has been delayed my manufacturer'

class ShippingDelayedException(SupplierException):
	message = 'Widget shipping has been delayed supplier'

class CheckoutException(WidgetException):
	message = 'Checkout exception'

class InventoryException(CheckoutException):
	message = 'Checkout Inventory Exception'

class OutOfStockException(InventoryException):
	message = 'Inventory out of stock'

class PricingException(CheckoutException):
	message = 'Checkout pricing exception'

class InvalidCouponCodeException(PricingException):
	message = 'Invalid checkout coupon code'

class CannotStackCouponException(PricingException):
	message = 'Cannot stack checkout coupon code'

# try:
# 	raise CannotStackCouponException()
# except CannotStackCouponException as ex:
# 	ex.log_exception()
# 	raise

from http import HTTPStatus
import json

class WidgetException(Exception):
	message = 'Generic Widget exception.'
	http_status = HTTPStatus.INTERNAL_SERVER_ERROR

	def __init__(self, *args, customer_message=None):
		super().__init__(args)
		if args:
			self.message = args[0]
		self.customer_message = customer_message if customer_message is not None else self.message

	def log_exception(self):
		exception = {
			'type': type(self).__name__,
			'message': self.message,
			'args': self.args[1:]
		}
		print(f'EXCEPTION: {datetime.now().isoformat()}: {exception}')

	def to_json(self):
		respone = {
		'code': self.http_status.value,
		'message': '{}: {}'.format(self.http_status.phrase, self.customer_message),
		'category': type(self).__name__,
		'time_now': datetime.now().isoformat()
		}
		return json.dumps(respone)

# e = WidgetException('some custom message for log and user')
# e.log_exception()
# print(e.to_json())
# e = WidgetException('custom internal message', customer_message='something custom user message')
# e.log_exception()
# print(e.to_json())



# try:
# 	raise WidgetException('Custom error message')
# except WidgetException as ex:
# 	print(repr(ex.__traceback__))

# import traceback

# try:
# 	raise ValueError
# except ValueError:
# 	try:
# 		raise WidgetException('Custom error message')
# 	except WidgetException as ex:
# 		tb = traceback.TracebackException.from_exception(ex)
# 		tb = ''.join(tb.format())
# 		print(tb)
# 		#print(list(tb.format()))