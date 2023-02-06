import copy
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

    # Create the tree
    stack = []
    for char in formula:
        if char.isalpha() and char.isupper():
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


def collapse_tree(root: Node) -> str:
    res = ""

    if root.name == "!":
        res += collapse_tree(root.children[0]) + root.name
    elif root.name == "&" or root.name == "|" or root.name == "^" or root.name == ">" or root.name == "=":
        res += collapse_tree(root.children[1]) + \
            collapse_tree(root.children[0]) + root.name
    else:
        res += root.name

    return res


def NNF_transform(root: Node) -> Node:

    root = copy.deepcopy(root)

    if root.name.isalpha() or root.name == "1" or root.name == "0":
        return root

    elif root.name == "!":
        if root.children[0].name == "!":
            root = NNF_transform(root.children[0].children[0])
        elif root.children[0].name == "&":
            left = NNF_transform(
                Node("!", children=[root.children[0].children[0]]))
            right = NNF_transform(
                Node("!", children=[root.children[0].children[0]]))
            ret = Node("|",
                       children=[left, right])
            root = ret
        elif root.children[0].name == "|":
            root = Node("&",
                        children=[NNF_transform(Node("!", children=[root.children[0].children[0]])),
                                  NNF_transform(
                            Node("!", children=[root.children[0].children[0]]))
                        ])
        else:
            root = Node("!", children=[NNF_transform(root.children[0])])

    elif root.name == ">":
        right = copy.deepcopy(root.children[0])
        left = copy.deepcopy(root.children[1])
        root = Node("|", children=[NNF_transform(right),
                                   NNF_transform(Node("!", children=[left]))
                                   ])

    elif root.name == "=":
        right = copy.deepcopy(root.children[0])
        left = copy.deepcopy(root.children[1])
        right_2 = copy.deepcopy(root.children[0])
        left_2 = copy.deepcopy(root.children[1])
        root = NNF_transform(Node("|", children=[
            NNF_transform(Node("&", children=[
                Node("!", children=[right]),
                Node("!", children=[left])
            ])),
            NNF_transform(Node("&", children=[right, left]))
        ]))

    return copy.deepcopy(root)


def negation_normal_form(formula: str, show_tree=False) -> str:
    tree = parse_formula(formula)

    tree = NNF_transform(tree)

    if show_tree:
        for pre, fill, node in RenderTree(tree):
            print("%s%s" % (pre, node.name))

    return collapse_tree(tree)


if __name__ == "__main__":
    print(negation_normal_form("AB&!", show_tree=True))
    print('*' * 25)
    print(negation_normal_form("AB|!", show_tree=True))
    print('*' * 25)
    print(negation_normal_form("AB>", show_tree=True))
    print('*' * 25)
    print(negation_normal_form("AB=", show_tree=True))
    print('*' * 25)
    print(negation_normal_form("AB|C&!", show_tree=True))
    print('*' * 25)

    assert negation_normal_form("AB&!") == "A!B!|"
    assert negation_normal_form("AB|!") == "A!B!&"
    assert negation_normal_form("AB>") == "A!B|"
    assert negation_normal_form("AB=") == "AB&A!B!&|"
    assert negation_normal_form("AB|C&!") == "A!B!&C!|"
