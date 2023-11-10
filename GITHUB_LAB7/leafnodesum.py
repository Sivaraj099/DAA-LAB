class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def leaf_node_sum(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return root.value

    return leaf_node_sum(root.left) + leaf_node_sum(root.right)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

result = leaf_node_sum(root)

print(f"Sum of leaf nodes: {result}")
