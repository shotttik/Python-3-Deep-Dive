'''
Tests the validator functions
Command line: python -m pytest tests/test_validators.py
'''

# import pytest
from validators import validate_integer

class TestIntegerValidator:
	def test_valid(self):
		validate_integer('arg', 10, 0, 20, 'Custom min message', 'custom max message')

	def test_type_error(self):
		with pytest.raises(TypeError):
			validate_integer('arg', 1.5)

	