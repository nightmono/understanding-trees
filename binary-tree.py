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

def preorder_traverse(node, level=0):
    """Pre-order traversal of all passed node and all its children."""

    if node is None:
        return
    
    print(f"{' '*2*level}{node.value}")
    level += 1
    preorder_traverse(node.left, level)
    preorder_traverse(node.right, level)

# Hard to read ;-;
#   +
#  / \
# 1   *
#    / \
#   2   3
# I would like some way to display trees.
root_node = Node("+", Node("1"), Node("*", Node(2), Node(3)))
print(root_node)

preorder_traverse(root_node)