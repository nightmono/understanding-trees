class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # The reason why I'm using passing the children into bool is because the
        # __repr__ would be recursive otherwise.
        # And look like this:
        # Node(+, left=Node(1, left=None, right=None), right=Node(*, left=Node(2, left=None, right=None), right=Node(3, left=None, right=None)))
        return f"Node({self.val}, left={bool(self.left)}, right={bool(self.right)})"

def postorder_travese_recursive(node: Node, postfix_list: list):
    if node is None:
        return

    postorder_travese_recursive(node.left, postfix_list)
    postorder_travese_recursive(node.right, postfix_list)
    postfix_list.append(node.val)

def preorder_traverse(node: Node):
    """Iterative pre-order traversal."""

    stack = [node]
    prefix = []

    while stack:
        node = stack.pop()
        prefix.append(node.val)
        # Push right child first so we pop (visit) the left node first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return prefix

def postorder_traverse(node: Node):
    """Iterative post-order traversal."""

    stack: list[Node] = []
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
                postfix.append(peek_node.val)
                last_visited_node = stack.pop()

    return postfix

def print_tree(node, level=0, prefix=""):
    if node != None:
        # Print right node first so tree is correctly rotated by -90 degrees.
        print_tree(node.right, level + 1, "/ ")
        print(" " * 3 * level + prefix + str(node.val))
        print_tree(node.left, level + 1, "\\ ")

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

print_tree(root_node)

print(preorder_traverse(root_node))
print(postorder_traverse(root_node))

the_list = []
postorder_travese_recursive(root_node, the_list)
print(the_list)