def eval_formula(formula: str) -> bool:
    """Evaluates a formula.
    Args:
        formula: A string representing a formula.
    Raises:
        TypeError: If the formula is not a string.
        ValueError: If the formula is invalid.
    Returns:
        Result of the formula evaluation as a boolean.
    """

    if not isinstance(formula, str):
        raise TypeError(f"Formula must be a string, not {type(formula)}")
    
    stack = []
    for char in formula:
        if char == '0':
            stack.append(False)
        elif char == '1':
            stack.append(True)
        elif char == '!':
            if len(stack) == 0:
                raise ValueError(f"Invalid formula '{formula}'")
            stack[-1] = not stack[-1]
        elif char == '&':
            if len(stack) < 2:
                raise ValueError(f"Invalid formula '{formula}'")
            stack[-2] = stack[-2] and stack[-1]
            stack.pop()
        elif char == '|':
            if len(stack) < 2:
                raise ValueError(f"Invalid formula '{formula}'")
            stack[-2] = stack[-2] or stack[-1]
            stack.pop()
        elif char == '^':
            if len(stack) < 2:
                raise ValueError(f"Invalid formula '{formula}'")
            stack[-2] = stack[-2] ^ stack[-1]
            stack.pop()
        elif char == '>':
            if len(stack) < 2:
                raise ValueError(f"Invalid formula '{formula}'")
            stack[-2] = not stack[-2] or stack[-1]
            stack.pop()
        elif char == '=':
            if len(stack) < 2:
                raise ValueError(f"Invalid formula '{formula}'")
            stack[-2] = (not stack[-2] or stack[-1]) and (not stack[-1] or stack[-2])
            stack.pop()
        else:
            raise ValueError(f"Invalid character '{char}' in formula")

    if len(stack) != 1:
        raise ValueError(f"Invalid formula '{formula}'")
    return stack[0]

if __name__ == "__main__":
    print(eval_formula("10&"))
    print(eval_formula("10|"))
    print(eval_formula("11>"))
    print(eval_formula("10="))
    print(eval_formula("1011||="))

    assert eval_formula("10&") == False
    assert eval_formula("10|") == True
    assert eval_formula("11>") == True
    assert eval_formula("10=") == False
    assert eval_formula("1011||=") == True