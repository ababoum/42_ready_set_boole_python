def gray_code(n: int) -> int:
	return n ^ (n >> 1)


if __name__ == "__main__":
	print(gray_code(0))
	print(gray_code(1))
	print(gray_code(2))
	print(gray_code(3))
	print(gray_code(4))
	print(gray_code(5))
	print(gray_code(6))
	print(gray_code(7))
	print(gray_code(8))

	assert gray_code(0) == 0
	assert gray_code(1) == 1
	assert gray_code(2) == 3
	assert gray_code(3) == 2
	assert gray_code(4) == 6
	assert gray_code(5) == 7
	assert gray_code(6) == 5
	assert gray_code(7) == 4
	assert gray_code(8) == 12
	