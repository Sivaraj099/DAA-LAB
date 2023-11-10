class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_bst(root, target):
    if not root or root.value == target:
        return root

    if target < root.value:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

result_node = search_bst(root, 4)

if result_node:
    print(f"Node with value 4 found: {result_node.value}")
else:
    print("Node with value 4 not found.")
