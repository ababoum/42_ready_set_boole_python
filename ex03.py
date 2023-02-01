from anytree import Node, RenderTree


# O(n) complexity -> One formula traversal
def parse_formula(formula: str, show_tree: bool = False) -> Node:
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

    # Check if the tree is valid
    if len(stack) != 1:
        raise ValueError(f"Invalid formula '{formula}'")

    if show_tree:
        for pre, fill, node in RenderTree(stack[0]):
            print("%s%s" % (pre, node.name))

    return stack[0]


# O(n) complexity -> One tree traversal
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


def eval_formula(formula: str, show_tree: bool = False) -> bool:
    """Evaluates a formula.
    Args:
        formula: A string representing a formula.
    Raises:
        TypeError: If the formula is not a string.
        ValueError: If the formula is invalid.
    Returns:
        Result of the formula evaluation as a boolean.
    """
    return eval_node(parse_formula(formula, show_tree=show_tree))


if __name__ == "__main__":
    print(eval_formula("10&", True))
    print('*' * 25)
    print(eval_formula("10|", True))
    print('*' * 25)
    print(eval_formula("11>", True))
    print('*' * 25)
    print(eval_formula("10=", True))
    print('*' * 25)
    print(eval_formula("1011||=", True))

    assert eval_formula("10&") == False
    assert eval_formula("10|") == True
    assert eval_formula("11>") == True
    assert eval_formula("10=") == False
    assert eval_formula("1011||=") == True
