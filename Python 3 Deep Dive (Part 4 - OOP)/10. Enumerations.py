# import enum

# class Color(enum.Enum):
# 	red = 1
# 	green = 2
# 	blue = 3

# class Status(enum.Enum):
# 	PENDING = 'pending'
# 	RUNNING = 'running'
# 	COMPLETED = 'completed'

# class UnitVector(enum.Enum):
# 	V1D = (1, )
# 	V2D = (1, 1)
# 	V3D = (1, 1, 1)

# Status.PENDING
# print(UnitVector.V3D.value)

# class NumSides(enum.Enum):
# 	Triangle = 3
# 	Rectangle = 4
# 	Square = 4
# 	Rhombus = 4
# print(NumSides.Rectangle is NumSides.Square)
# print(NumSides.Rhombus is NumSides.Square)
# print(NumSides.Rectangle in NumSides)
# print(NumSides.__members__)
# print(list(NumSides))

# class Status(enum.Enum):
# 	read = 'ready'

# 	running = 'running'
# 	busy = 'running'
# 	processing = 'running'


from enum import Enum

class Color(Enum):
	red = 1
	green = 2
	blue = 3

	def purecolor(self, value):
		return {self : value}

	def __repr__(self):
		return f'{self.name} ({self.value})'

print(Color.red.purecolor(100))

print(Color.red)