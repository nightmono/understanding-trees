class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_value(node, val):
    if node is None:
        node = Node(val)
    elif node.val > val:
        node.left = insert_value(node.left, val)
    else:
        node.right = insert_value(node.right, val)
    return node

def main():
    root_node = Node(5)
    insert_value(root_node, 3)
    insert_value(root_node, 6)
    insert_value(root_node, 2)
    insert_value(root_node, 7)
    insert_value(root_node, 3)

if __name__ == "__main__":
    main()