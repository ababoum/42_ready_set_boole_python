from anytree import Node, RenderTree


def parse(formula: str) -> Node:
    """Parses a formula.
    Args:
        formula: A string representing a formula.
    Raises:
        TypeError: If the formula is not a string.
        ValueError: If the formula is invalid.
    Returns:
        The root node of the formula tree.
    """
    if not isinstance(formula, str):
        raise TypeError(f"Formula must be a string, not {type(formula)}")
    if any(char not in '01!&|^>=' for char in formula):
        raise ValueError(f"Invalid formula '{formula}'")

    # Create the tree

    stack = []
    for char in formula:
        if char == '0' or char == '1':
            stack.append(Node(char))
        elif char == '!':
            if len(stack) == 0:
                raise ValueError(f"Invalid formula '{formula}'")
            stack.append(Node(char, children=[stack.pop()]))
        elif char == '&':
            if len(stack) < 2:
                raise ValueError(f"Invalid formula '{formula}'")
            stack.append(Node(char, children=[stack.pop(), stack.pop()]))
        elif char == '|':
            if len(stack) < 2:
                raise ValueError(f"Invalid formula '{formula}'")
            stack.append(Node(char, children=[stack.pop(), stack.pop()]))
        elif char == '^':
            if len(stack) < 2:
                raise ValueError(f"Invalid formula '{formula}'")
            stack.append(Node(char, children=[stack.pop(), stack.pop()]))
        elif char == '>':
            if len(stack) < 2:
                raise ValueError(f"Invalid formula '{formula}'")
            stack.append(Node(char, children=[stack.pop(), stack.pop()]))
        elif char == '=':
            if len(stack) < 2:
                raise ValueError(f"Invalid formula '{formula}'")
            stack.append(Node(char, children=[stack.pop(), stack.pop()]))
        else:
            raise ValueError(f"Invalid character '{char}' in formula")

    return stack[0]


def eval_node(node: Node) -> bool:
    """Evaluates a node.
    Args:
        node: A node representing a formula.
    Raises:
        TypeError: If the node is not a Node.
        ValueError: If the node is invalid.
    Returns:
        Result of the formula evaluation as a boolean.
    """
    if not isinstance(node, Node):
        raise TypeError(f"Node must be a Node, not {type(node)}")
    if node.is_leaf:
        if node.name == '0':
            return False
        elif node.name == '1':
            return True
        else:
            raise ValueError(f"Invalid node '{node.name}'")
    elif node.name == '!':
        return not eval_node(node.children[0])
    elif node.name == '&':
        return eval_node(node.children[0]) and eval_node(node.children[1])
    elif node.name == '|':
        return eval_node(node.children[0]) or eval_node(node.children[1])
    elif node.name == '^':
        return eval_node(node.children[0]) ^ eval_node(node.children[1])
    elif node.name == '>':
        return not eval_node(node.children[0]) or eval_node(node.children[1])
    elif node.name == '=':
        return (not eval_node(node.children[0]) or eval_node(node.children[1])) and (not eval_node(node.children[1]) or eval_node(node.children[0]))
    else:
        raise ValueError(f"Invalid node '{node.name}'")


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
            stack[-2] = (not stack[-2] or stack[-1]
                         ) and (not stack[-1] or stack[-2])
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
