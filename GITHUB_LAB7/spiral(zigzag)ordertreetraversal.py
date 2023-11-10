class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def spiral_order_traversal(root):
    if not root:
        return []

    result = []
    queue = [root]
    left_to_right = True

    while queue:
        level_size = len(queue)
        level_values = []

        for _ in range(level_size):
            if left_to_right:
                node = queue.pop(0)
                level_values.append(node.value)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            else:
                node = queue.pop()
                level_values.append(node.value)
                if node.right: queue.insert(0, node.right)
                if node.left: queue.insert(0, node.left)

        result.append(level_values)
        left_to_right = not left_to_right

    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

result = spiral_order_traversal(root)

print("Spiral Order Traversal:")
for level in result:
    print(level)
