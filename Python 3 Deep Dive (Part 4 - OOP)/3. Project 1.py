import numbers
from datetime import timedelta
from datetime import datetime
import itertools
from collections import namedtuple


class TimeZone:
	def __init__(self, name, offset_hours, offset_minutes):
		if name is None or len(str(name).strip()) == 0:
			raise ValueError('TimeZone name cannot be empty')

		self._name = str(name).strip()

		if not isinstance(offset_hours, numbers.Integral):
			raise ValueError("Hour offset must be an Integer.")

		if not isinstance(offset_minutes, numbers.Integral):
			raise ValueError("Minute offset must be an Integer.")

		if offset_minutes > 59 or offset_minutes < -59:
			raise ValueError('Minutes offset must be between -59 and 59 (inclusive)')

		offset = timedelta(hours=offset_hours, minutes=offset_minutes)
		if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
			raise ValueError('Offset must be between -12:00 and +14:00')

		self._offset_hour = offset_hours
		self._offset_minutes = offset_minutes
		self._offset = offset

	#readonly property
	@property
	def offset(self):
		return self._offset

	#readonly property
	@property
	def name(self):
		return self._name
		
	def __eq__(self, other):
		return (isinstance(other, TimeZone) and
			self.name == other.name and
			self._offset_hour == other._offset_hours and
			self._offset_minutes == other._offset_minutes)

	def __repr__(self):
		return (f'TimeZone(name="{self.name}",'
		 f'offset_hours={self._offset_hour},'
		 f'offset_minutes{self._offset_minutes})')


Confirmation = namedtuple('Confirmation', 'account_number tranasction_code transaction_id time_utc time')


class Account:


	transaction_counter = itertools.count(100)
	_interest_rate = 0.5 # percent
	_transaction_codes = {
		'deposit': 'D',
		'withdraw': 'W',
		'interest': 'I',
		'rejected': 'X'
	}

	def __init__(self, account_number, first_name, last_name,
		timezone = None, initial_balance=0):
		self._account_number = account_number
		self.first_name = first_name
		self.last_name = last_name

		if timezone is None:
			timezone = TimeZone('UTC', 0, 0)
		self.timezone = timezone

		# we should use decimal instead of float
		self._balance = float(initial_balance)

	@property
	def account_number(self):
		return self._account_number

	@property
	def first_name(self):
		return self._first_name

	@first_name.setter
	def first_name(self, value):
		self.validate_and_set_name('_first_name', value, 'First name')

	@property
	def last_name(self):
		return self._last_name

	@last_name.setter
	def last_name(self, value):
		self.validate_and_set_name('_last_name', value, 'Last name')

	@property
	def full_name(self):
		return f'{self.first_name} {self.last_name}'

	@property
	def balance(self):
		return self._balance
	
	@property
	def timezone(self):
		return self._timezone
	
	@timezone.setter
	def timezone(self, value):
		if not isinstance(value, TimeZone):
			raise ValueError('Time Zone must be a valid TimeZone object')
		self._timezone = value

	@classmethod
	def get_interest_rate(cls):
		return cls._interest_rate

	@classmethod
	def set_interest_rate(cls, value):
		if not isinstance(value, numbers.Real):
			raise ValueError('Interest rate must be a real number.')

		if value < 0:
			raise ValueError('Interest rate cannot be negative')
		cls._interest_rate = value

	@staticmethod
	def validate_real_number(value, min_value=None):
		if not isinstance(value, numbers.Real):
			raise ValueError('Value Must be a real number.')

		if min_value is not None and value < min_value:
			raise ValueError(f'Value must be at least {min_value}')

		return value

	def generate_confirmation_code(self,  tranasction_code):
		dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
		return f'{tranasction_code}-{self.account_number}-{dt_str}-{next(Account.transaction_counter)}'

	def validate_and_set_name(self, property_name, value, field_title):
		if value is None or len(str(value).strip()) == 0:
			raise ValueError(f'{field_title} cannot be empty.')
		setattr(self, property_name, value)

	def make_transaction(self):
		return self.generate_confirmation_code('dummy')

	@staticmethod
	def parse_confirmation_code(confirmation_code, preferred_time_zone=None):
		# dummy-A100-20190405291350-101
		parts = confirmation_code.split('-')
		if len(parts) != 4:
			raise ValueError('Invalid confirmation Code')
		transaction_code, account_number, raw_dt_utc, transaction_id = parts

		try:
			dt_utc = datetime.strptime(raw_dt_utc, '%Y%m%d%H%M%S')
		except ValueError as ex:
			raise ValueError('Invalid transaction Datetime.') from ex

		if preferred_time_zone is None:
			preferred_time_zone = TimeZone('UTC', 0, 0)

		if not isinstance(preferred_time_zone, TimeZone):
			raise ValueError('Invalid TimeZone specified.')

		dt_preferred = dt_utc + preferred_time_zone.offset
		dt_preferred_str = f"{dt_preferred.strftime('%Y-%m-%d %H:%M:%S')} ({preferred_time_zone.name})"

		return Confirmation(account_number, transaction_code,
		 transaction_id, dt_utc.isoformat(), dt_preferred_str)

	def deposit(self, value):
		value = Account.validate_real_number(value, 0.01) # itsnot right.

		tranasction_code = Account._transaction_codes['deposit']
		conf_code = self.generate_confirmation_code(tranasction_code)
		self._balance += value
		return conf_code

	def withdraw(self, value):
		value = Account.validate_real_number(value, 0.01) # itsnot right.
		accepted = False
		if self.balance - value < 0:
			# insufficient fund

			transaction_code = Account._transaction_codes['rejected']
		else:
			accepted = True
			transaction_code = Account._transaction_codes['withdraw']

		conf_code = self.generate_confirmation_code(transaction_code)

		if accepted:
			self._balance -= value

		return conf_code

	def pay_interest(self):
		interest = self.balance * Account.get_interest_rate() / 100
		conf_code = self.generate_confirmation_code(self._transaction_codes['interest'])
		self._balance += interest
		return conf_code

a = Account('A100', 'Eric', 'Idle', timezone=TimeZone('MST', -7, 0), initial_balance=100)
print(a.balance)
print(a.deposit(150.02))
print(a.balance)
print(a.withdraw(0.02))
print(a.balance)
Account.set_interest_rate(1.0)
print(a.get_interest_rate())
print(a.pay_interest())
print(a.balance)
print(a.withdraw(1000))