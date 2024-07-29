class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функція для знаходження найбільшого значення у бінарному дереві пошуку
def find_max_value(node):
    # Починаємо з кореневого вузла і рухаємося вправо, поки можливо
    current = node
    while current.right is not None:
        current = current.right
    return current.val

# Приклад використання функції з простим бінарним деревом пошуку
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.right = TreeNode(30)

print("Найбільше значення у дереві пошуку:", find_max_value(root))
