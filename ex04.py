# O(log n) time complexity
def append_on_all(stacks, value):
    for stack in stacks:
        stack.append(value)

# O(n) time complexity


def check_formula(formula: str) -> bool:
    if any(char not in '!&|^>=' or not char.isalpha() for char in formula):
        return False
    return True


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
    if not check_formula(formula):
        raise ValueError(f"Invalid formula '{formula}'")

    # Get the variables in the formula
    formulas = []
    variables = set()
    for char in formula:
        if char.isalpha() and char.isupper() and char not in variables:
            variables.add(char)
            stacks.append(*stacks)
            append_on_all(stacks[0:len(stacks) // 2], False)
            append_on_all(stacks[len(stacks) // 2:], True)
        
