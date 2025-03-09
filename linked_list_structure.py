class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None  # Pointer to left child
        self.right = None  # Pointer to right child

    def __repr__(self):
        return str(self.value)


# Example of building a simple binary tree manually
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

root.left.left = TreeNode(2)
root.left.right = TreeNode(7)

root.right.left = TreeNode(12)
root.right.right = TreeNode(18)


# In-order Traversal (Left -> Root -> Right)
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)


print("In-order Traversal of the Tree:")
inorder_traversal(root)
