# Function definition for type
from triangle import type_of_triangle

def test_type_of_triangle():
	expected_type = 'Equilateral'
	actual_type = type_of_triangle(1, 1, 1)
	assert actual_type == expected_type