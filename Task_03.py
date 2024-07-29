class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функція для знаходження суми всіх значень у бінарному дереві пошуку
def sum_tree_values(node):
    if node is None:
        return 0
    return node.val + sum_tree_values(node.left) + sum_tree_values(node.right)

# Приклад використання функції з простим бінарним деревом пошуку
root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(1)
root.right = TreeNode(20)
root.right.left = TreeNode(15)

print("Сума всіх значень у дереві пошуку:", sum_tree_values(root))
