from calculator import add, subtract, multiply, divide

def test_add():
	assert add(2, 3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_subtract():
	assert subtract(9, 4) == 5

def test_multiply():
	assert multiply(4, 5) == 20

def test_multiply_uneven():
	#Arrange
	a, b = 8, 0

	#Act
	result = multiply(a, b)

	#Assert
	assert result == 0

