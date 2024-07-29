class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функція для знаходження найменшого значення у бінарному дереві пошуку
def find_min_value(node):
    # Починаємо з кореневого вузла і рухаємося вліво, поки можливо
    current = node
    while current.left is not None:
        current = current.left
    return current.val

# Приклад використання функції з простим бінарним деревом пошуку
root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(1)
root.right = TreeNode(20)

print("Найменше значення у дереві пошуку:", find_min_value(root))
