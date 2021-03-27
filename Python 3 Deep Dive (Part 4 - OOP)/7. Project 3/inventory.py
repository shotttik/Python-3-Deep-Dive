"""Inventory Models"""

from validators import validate_integer


class Resource:
	"""Base class for resources"""
	def __init__(self, name, manufacturer, total, allocated):
		self._name = name
		self._manufacturer = manufacturer

		validate_integer('total', total, min_value=0)
		self._total = total

		validate_integer('allocated', allocated, 0, total,
			custom_max_message='allocated Inventory cannot exceed total inventory')
		self._allocated = allocated

	@property
	def name(self):
		"""

		Returns:
			str: the resource name
		"""
		return self._name

	@property
	def manufacturer(self):
		"""

		Returns:
			str: the resource manufacturer
		"""
		return self._manufacturer

	@property
	def total(self):
		"""

		Returns:
			int: the total inventory count
		"""		
		return self._total
	
	@property
	def allocated(self):
		"""

		Returns:
			int: number of resources in use
		"""		
		return self._allocated
		
	@property
	def category(self):
		"""

		Returns:
			str: the resource category
		"""		
		return type(self).__name__.lower()
	
	@property
	def available(self):
		"""

		Returns:
			int: number of resources available for use
		"""		
		return self.total - self.allocated

	def __str__(self):
		return self.name
	
	def __repr__(self):
		return (f'{self.name} ({self.category} - {self.manufacturer}) : '
			f'total={self.total}, allocated={self.allocated}'
			)

	def claim(self, num):
		"""
		Claim n invetory items (if available)

		Args:
			num (int): Number of inventory items to claim

		Returns:

		"""
		validate_integer('num', num, 1, self.available,
			custom_max_message="Cannot Claim more than available")
		self._allocated += num

	def freeup(self, num):
		"""
		Return an inventory item to the available pool
		Args:
			num (int): Number of items to return (cannot exceed number in use)
		Returns:

		"""
		validate_integer('num', num, 1, self.allocated,
			custom_max_message='Cannot return more than allocated')
		self._allocated -=num

	def died(self, num):
		"""
		Number of items to dellocate and remove from inventory pool
		alltogether

		Args:
			num (int): number of items that have died

		Returns:

		"""
		validate_integer('num', num, 1, self.allocated,
			custom_max_message='cannot retire more than allocated'
			 )
		self._total -= num
		self._allocated -= num

	def purchased(self, num):
		"""
		Add new ivnentory to the pool.

		Args:
			num (int): Number of items to add to the pool

		Returns:

		"""
		validate_integer('num', num, 1)
		self._total += num

class CPU(Resource):
	"""Resource subclass used to track specific CPU inventory pools"""

	def __init__(
		self, name, manufacturer, total, allocated,
		cores, socket, power_watts
		):
		"""
		Args:
			Doc string about this CPU class...
		"""
		super().init(name, manufacturer, total, allocated)

		validate_integer('cores', cores, 1)
		validate_integer('power_watts', power_watts, 1)

		self._cores = cores
		self._socket = socket
		self._power_watts = power_watts

	@property
	def cores(self):
		"""
		Number of cores.

		Returns:
			int
		"""
		return self._cores

	@property
	def socket(self):
		"""
		the socket type for this cpu

		Returns:
			str
		"""
		return self._socket

	@property
	def power_watts(self):
		"""
		The rated wattage of this CPU

		Returns:
			int
		"""
		return self._power_watts
		
	def __repr__(self):
		return f'{self.category}: {self.name} ({self.socket} - x{self.cores})'

	