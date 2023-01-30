def print_truth_table(formula: str) -> None:
	"""Prints the truth table of a given formula.
	Args:
		formula: The formula to print the truth table of.
	Raises:
		TypeError: If the formula is not a string.
		ValueError: If the formula is invalid.
	"""
	if not isinstance(formula, str):
		raise TypeError(f"Formula must be a string, not {type(formula)}")

	# Get the variables in the formula
	
	stacks = []
	variables = set()
	for char in formula:
		if char.isalpha() and char.isupper() and char not in variables:
			variables.add(char)
			stacks.append([])
			stacks[-1].append(False)
			stacks.append([])
			stacks[-1].append(True)
		elif char not in "01&|!^>=":
			raise ValueError(f"Invalid character '{char}' in formula")
		
