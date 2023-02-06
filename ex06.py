import copy
from anytree import Node, RenderTree

# in anytree, the right child is the first child in the list (index 0)

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
        left = copy.deepcopy(root.children[0])
        right = copy.deepcopy(root.children[1])
        left_2 = copy.deepcopy(root.children[0])
        right_2 = copy.deepcopy(root.children[1])
        root = NNF_transform(Node("&", children=[
            NNF_transform(
                Node(">", children=[left, right])),
            NNF_transform(
                Node(">", children=[right_2, left_2]))
        ]))

    elif root.name == '&':
        if root.children[1].name == '&' and root.children[0].name != '&':
            root = Node('&', children=[NNF_transform(root.children[1]),
                                    NNF_transform(root.children[0])])

    # elif root.name == '&':
    #     if root.children[0].name == '|':
    #         common = copy.deepcopy(root.children[1])
    #         left = copy.deepcopy(root.children[0].children[0])
    #         right = copy.deepcopy(root.children[0].children[1])
    #         root = Node('|', children=[
    #             NNF_transform(
    #                 Node('&', children=[NNF_transform(common), NNF_transform(left)])),
    #             NNF_transform(
    #                 Node('&', children=[NNF_transform(common), NNF_transform(right)]))
    #         ])
    #     elif root.children[1].name == '|':
    #         common = copy.deepcopy(root.children[0])
    #         left = copy.deepcopy(root.children[1].children[0])
    #         right = copy.deepcopy(root.children[1].children[1])
    #         root = Node('|', children=[
    #             NNF_transform(
    #                 Node('&', children=[NNF_transform(common), NNF_transform(left)])),
    #             NNF_transform(
    #                 Node('&', children=[NNF_transform(common), NNF_transform(right)]))
    #         ])
    #     elif root.children[0].name == '0':
    #         root = Node('0')
    #     elif root.children[1].name == '0':
    #         root = Node('0')
    #     elif root.children[0].name == '1':
    #         root = NNF_transform(root.children[1])
    #     elif root.children[1].name == '1':
    #         root = NNF_transform(root.children[0])
    #     else:
    #         left = NNF_transform(root.children[0])
    #         right = NNF_transform(root.children[1])

    #         # tautology
    #         if left.name.isalpha() and right.name == '!' and right.children[0].name.isalpha():
    #             if left.name == right.children[0].name:
    #                 root = Node('0')
    #         elif right.name.isalpha() and left.name == '!' and left.children[0].name.isalpha():
    #             if right.name == left.children[0].name:
    #                 root = Node('0')

    elif root.name == '|':
        if root.children[0].name == '&':
            common = copy.deepcopy(root.children[1])
            left = copy.deepcopy(root.children[0].children[0])
            right = copy.deepcopy(root.children[0].children[1])
            root = Node('&', children=[
                NNF_transform(
                    Node('|', children=[NNF_transform(common), NNF_transform(left)])),
                NNF_transform(
                    Node('|', children=[NNF_transform(common), NNF_transform(right)]))
            ])
        elif root.children[1].name == '&':
            common = copy.deepcopy(root.children[0])
            left = copy.deepcopy(root.children[1].children[0])
            right = copy.deepcopy(root.children[1].children[1])
            root = Node('&', children=[
                NNF_transform(
                    Node('|', children=[NNF_transform(common), NNF_transform(left)])),
                NNF_transform(
                    Node('|', children=[NNF_transform(common), NNF_transform(right)]))
            ])
        elif root.children[0].name == '1':
            root = Node('1')
        elif root.children[1].name == '1':
            root = Node('1')
        elif root.children[0].name == '0':
            root = NNF_transform(root.children[1])
        elif root.children[1].name == '0':
            root = NNF_transform(root.children[0])
        else:
            left = NNF_transform(root.children[0])
            right = NNF_transform(root.children[1])

            # tautology
            if left.name.isalpha() and right.name == '!' and right.children[0].name.isalpha():
                if left.name == right.children[0].name:
                    root = Node('1')
            elif right.name.isalpha() and left.name == '!' and left.children[0].name.isalpha():
                if right.name == left.children[0].name:
                    root = Node('1')

    return copy.deepcopy(root)


def conjunctive_normal_form(formula: str, show_tree=False) -> str:
    tree = parse_formula(formula)

    tree = NNF_transform(tree)

    if show_tree:
        for pre, fill, node in RenderTree(tree):
            print("%s%s" % (pre, node.name))

    return collapse_tree(tree)


if __name__ == "__main__":
    # print(conjunctive_normal_form("AB&!"))
    # print('*' * 25)
    # print(conjunctive_normal_form("AB|!"))
    # print('*' * 25)
    # print(conjunctive_normal_form("AB|C&"))
    # print('*' * 25)
    # print(conjunctive_normal_form("AB|C|D|"))
    # print('*' * 25)
    print(conjunctive_normal_form("AB&C&D&", show_tree=True))
    print('*' * 25)
    # print(conjunctive_normal_form("AB&!C!|"))
    # print('*' * 25)
    # print(conjunctive_normal_form("AB|!C!&"))
    # print('*' * 25)

    # assert conjunctive_normal_form("AB&!") == "A!B!|"
    # assert conjunctive_normal_form("AB|!") == "A!B!&"
    # assert conjunctive_normal_form("AB|C&") == "AB|C&"
    # assert conjunctive_normal_form("AB|C|D|") == "AB|C|D|"
    assert conjunctive_normal_form("AB&C&D&") == "ABCD&&&"
    # assert conjunctive_normal_form("AB&!C!|") == "A!B!C!||"
    # assert conjunctive_normal_form("AB|!C!&") == "A!B!C!&&"