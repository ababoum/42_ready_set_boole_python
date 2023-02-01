from anytree import Node, RenderTree
from ex03 import parse_formula, eval_node, eval_formula
import copy


def print_truth_table(formula: str) -> None:
    """Evaluates a formula.
    Args:
        formula: A string representing a formula.
    Raises:
        TypeError: If the formula is not a string.
        ValueError: If the formula is invalid.
    Returns:
        Result of the formula evaluation as a boolean.
    """

    # Check if the formula is valid variables-wise
    alphabet = list()
    for char in formula:
        if char.isalpha() and char.isupper():
            alphabet.append(char)

    print(f"Truth table for formula '{formula}'")
    print(f"| {' | '.join(alphabet)} | = |")
    print(f"|{'|'.join(['---'] * (1 + len(alphabet)))}|")

    for i in range(2 ** len(alphabet)):
        formula_c = copy.copy(formula)
        # O(1) because the alphabet is always the same (<26)
        for char in alphabet[::-1]:
            if i % 2 == 0:
                formula_c = formula_c.replace(char, '0')
            else:
                formula_c = formula_c.replace(char, '1')
            i //= 2
        print(
            f"| {' | '.join(filter(lambda x: x.isnumeric(), formula_c))} | {(0,1)[eval_formula(formula_c)]} |")


if __name__ == "__main__":
    print_truth_table('AB&')
    print('*' * 25)
    print_truth_table('AB|')
    print('*' * 25)
    print_truth_table('A')
    print('*' * 25)
    print_truth_table('AB&C|')
    print('*' * 25)
    try:
        print_truth_table('A^C|')
    except ValueError as e:
        print(e)
