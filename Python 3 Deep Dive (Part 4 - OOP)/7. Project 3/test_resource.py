"""
Test for Resource class
Command line: python -m pytest test_resource.py
"""

import pytest
import inventory


@pytest.fixture
def resource_values():
	return {
		'name': 'Parrot',
		'manufacturer': 'Pirates',
		'total': 100,
		'allocated': 50
	}

@pytest.fixture
def resource(resource_values):
	return inventory.Resource(**resource_values)


def test_create_resource(resource_values):
	for attr_name in resource_values:
		assert getattr(resource, attr_name) == resource_values.get(attr_name)
	# assert resource.name == resource_values['name']
	# assert resource.manufacturer == resource_values['manufacturer']
	# assert resource.total == resource_values['total']
	# assert resource.allocated == resource_values['allocated']


def test_create_invalid_total_type(): 
	with pytest.raises(TypeError):	# this test should fail
		inventory.Resource('Parrot', 'Pirates', 10.5, 5)

def test_create_invalid_allocated_type(): 
	with pytest.raises(TypeError):	# this test should fail
		inventory.Resource('Parrot', 'Pirates', 10.5, 2.5)

def test_create_invalid_total_value(): 
	with pytest.raises(ValueError):	# this test should fail
		inventory.Resource('Parrot', 'Pirates', -10, 0)

@pytest.mark.parametrize('total, allocated', [(10, -5), (10, 20)])
def test_create_invalid_allocated_value(total, allocated):
	with pytest.raises(ValueError):
		inventory.Resource('Parrot', 'Pirates', total, allocated)


# and other tests....