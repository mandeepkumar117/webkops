
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# User se root ki value
root_value = int(input("Enter root value: "))
root = Node(root_value)


# Root ke left aur right children
left_value = int(input("Enter left child of root: "))
root.left = Node(left_value)

right_value = int(input("Enter right child of root: "))
root.right = Node(right_value)


# Left child ke children
left_left_value = int(input("Enter left child of " + str(left_value) + ": "))
root.left.left = Node(left_left_value)

left_right_value = int(input("Enter right child of " + str(left_value) + ": "))
root.left.right = Node(left_right_value)


# Right child ke children
right_left_value = int(input("Enter left child of " + str(right_value) + ": "))
root.right.left = Node(right_left_value)

right_right_value = int(input("Enter right child of " + str(right_value) + ": "))
root.right.right = Node(right_right_value)


# Preorder: Root -> Left -> Right
def preorder(node):
    if node is None:
        return

    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)


# Inorder: Left -> Root -> Right
def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)


# Postorder: Left -> Right -> Root
def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")


# Traversal output
print("\n\nPreorder Traversal:")
preorder(root)

print("\n\nInorder Traversal:")
inorder(root)

print("\n\nPostorder Traversal:")
postorder(root)

print()


# Enter root value: 1
# Enter left child of root: 2
# Enter right child of root: 3
# Enter left child of 2: 4
# Enter right child of 2: 5
# Enter left child of 3: 6
# Enter right child of 3: 7