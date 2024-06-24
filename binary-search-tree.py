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

# Taken from `binary-tree.py`.
def print_tree(node, level=0, prefix=""):
    if node != None:
        print_tree(node.right, level + 1, "/ ")
        print(" " * 3 * level + prefix + str(node.val))
        print_tree(node.left, level + 1, "\\ ")

def main():
    root_node = Node(5)
    insert_value(root_node, 3)
    insert_value(root_node, 6)
    insert_value(root_node, 2)
    insert_value(root_node, 7)
    insert_value(root_node, 3)
    
    print_tree(root_node)

if __name__ == "__main__":
    main()