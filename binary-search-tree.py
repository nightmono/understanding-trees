from binarytree import print_tree, Node

def insert_value(node, val):
    if node is None:
        node = Node(val)
    elif node.val > val:
        node.left = insert_value(node.left, val)
    else:
        node.right = insert_value(node.right, val)
    return node

def main():
    import random
    
    nums = [i for i in range(20)]
    random.shuffle(nums)
    
    root_node = Node(nums[0])
    for i in range(1, len(nums)):
        insert_value(root_node, nums[i])
    
    print_tree(root_node)

if __name__ == "__main__":
    main()