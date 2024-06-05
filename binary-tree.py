class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        # The reason why I'm using passing the children into bool is because the
        # __repr__ would be recursive otherwise.
        # And look like this:
        # Node(+, left=Node(1, left=None, right=None), right=Node(*, left=Node(2, left=None, right=None), right=Node(3, left=None, right=None)))
        return f"Node({self.value}, left={bool(self.left)}, right={bool(self.right)})"


def print_tree_levels(node, level=0):
    """Print tree nodes and their levels using preorder traversal."""

    if node is None:
        return

    print(f"{' '*2*level}{node.value}")
    level += 1
    print_tree_levels(node.left, level)
    print_tree_levels(node.right, level)

def postorder_travese_recursive(node: Node, postfix_list: list):
    if node is None:
        return

    postorder_travese_recursive(node.left, postfix_list)
    postorder_travese_recursive(node.right, postfix_list)
    postfix_list.append(node.value)

def preorder_traverse(node: Node):
    """Iterative pre-order traversal."""

    stack = [node]
    prefix = []

    while stack:
        node = stack.pop()
        prefix.append(node.value)
        # Push right child first so we pop (visit) the left node first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return prefix

def postorder_traverse(node: Node):
    """Iterative post-order traversal."""

    stack = []
    last_visited_node: Node = None
    postfix = []

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            peek_node = stack[-1]
            if peek_node.right and peek_node.right != last_visited_node:
                node = peek_node.right
            else:
                postfix.append(peek_node.value)
                last_visited_node = stack.pop()

    return postfix

# Hard to read ;-;
#   +
#  / \
# 1   *
#    / \
#   2   3
# I would like some way to display trees.
# root_node = Node("+", Node("1"), Node("*", Node("2"), Node("3")))
# This looks neater.
root_node = Node("+")
root_node.left = Node("1")
root_node.right = Node("*")
root_node.right.left = Node("2")
root_node.right.right = Node("3")

print_tree_levels(root_node)

print(preorder_traverse(root_node))
print(postorder_traverse(root_node))

the_list = []
postorder_travese_recursive(root_node, the_list)
print(the_list)