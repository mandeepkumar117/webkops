
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(numbers, i=0):

    if i >= len(numbers):
        return None

    root = Node(numbers[i])

    root.left = build_tree(numbers, 2 * i + 1)
    root.right = build_tree(numbers, 2 * i + 2)

    return root


# Preorder: Root -> Left -> Right
def preorder(root):

    if root is None:
        return

    print(root.data, end=" ")

    preorder(root.left)
    preorder(root.right)


# Inorder: Left -> Root -> Right
def inorder(root):

    if root is None:
        return

    inorder(root.left)

    print(root.data, end=" ")

    inorder(root.right)


# Postorder: Left -> Right -> Root
def postorder(root):

    if root is None:
        return

    postorder(root.left)
    postorder(root.right)

    print(root.data, end=" ")


# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 23, 24]

# Automatically create Binary Tree
root = build_tree(numbers)


# Tree ki kuch values print karna
print("Root:", root.data)
print("Left child:", root.left.data)
print("Right child:", root.right.data)
print("Left child of 2:", root.left.left.data)
print("Right child of 2:", root.left.right.data)


# Traversals
print("\nPreorder Traversal:")
preorder(root)

print("\n\nInorder Traversal:")
inorder(root)

print("\n\nPostorder Traversal:")
postorder(root)

print()
