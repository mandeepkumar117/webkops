
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


# Height calculate karna
def get_height(root):
    if root is None:
        return 0
    return root.height


# Balance factor calculate karna
def get_balance(root):
    if root is None:
        return 0
    return get_height(root.left) - get_height(root.right)


# Right Rotation
def right_rotate(y):
    x = y.left
    temp = x.right

    x.right = y
    y.left = temp

    y.height = 1 + max(
        get_height(y.left),
        get_height(y.right)
    )

    x.height = 1 + max(
        get_height(x.left),
        get_height(x.right)
    )

    return x


# Left Rotation
def left_rotate(x):
    y = x.right
    temp = y.left

    y.left = x
    x.right = temp

    x.height = 1 + max(
        get_height(x.left),
        get_height(x.right)
    )

    y.height = 1 + max(
        get_height(y.left),
        get_height(y.right)
    )

    return y


# Insert operation
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    else:
        return root

    root.height = 1 + max(
        get_height(root.left),
        get_height(root.right)
    )

    balance = get_balance(root)

    # LL Case
    if balance > 1 and data < root.left.data:
        return right_rotate(root)

    # RR Case
    if balance < -1 and data > root.right.data:
        return left_rotate(root)

    # LR Case
    if balance > 1 and data > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RL Case
    if balance < -1 and data < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


# Search operation
def search(root, data):
    if root is None:
        return False

    if root.data == data:
        return True

    if data < root.data:
        return search(root.left, data)

    return search(root.right, data)


# Minimum node find karna
def find_min(root):
    while root.left is not None:
        root = root.left
    return root


# Delete operation
def delete(root, data):
    if root is None:
        return None

    if data < root.data:
        root.left = delete(root.left, data)

    elif data > root.data:
        root.right = delete(root.right, data)

    else:
        # No left child
        if root.left is None:
            return root.right

        # No right child
        if root.right is None:
            return root.left

        # Two children
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    # Deleted node ke baad subtree empty ho sakta hai
    if root is None:
        return None

    # Height update
    root.height = 1 + max(
        get_height(root.left),
        get_height(root.right)
    )

    # Balance factor
    balance = get_balance(root)

    # LL Case
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)

    # LR Case
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RR Case
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)

    # RL Case
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


# Update operation
def update(root, old_value, new_value):
    if not search(root, old_value):
        print("Old value not found!")
        return root

    if old_value == new_value:
        print("Old and new values are the same!")
        return root

    if search(root, new_value):
        print("New value already exists!")
        return root

    root = delete(root, old_value)
    root = insert(root, new_value)

    print("Value updated successfully!")
    return root


# Inorder: Left, Root, Right
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# Preorder: Root, Left, Right
def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


# Postorder: Left, Right, Root
def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


# Main Program
root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    value = int(input("Enter value: "))
    root = insert(root, value)


# Menu System
while True:
    print("\n\n--- AVL TREE MENU ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    print("4. Search")
    print("5. Inorder Traversal")
    print("6. Preorder Traversal")
    print("7. Postorder Traversal")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = int(input("Enter value to insert: "))

        if search(root, value):
            print("Value already exists!")
        else:
            root = insert(root, value)
            print("Value inserted successfully!")

    elif choice == "2":
        value = int(input("Enter value to delete: "))

        if search(root, value):
            root = delete(root, value)
            print("Value deleted successfully!")
        else:
            print("Value not found!")

    elif choice == "3":
        old_value = int(input("Enter old value: "))
        new_value = int(input("Enter new value: "))
        root = update(root, old_value, new_value)

    elif choice == "4":
        value = int(input("Enter value to search: "))

        if search(root, value):
            print("Value found!")
        else:
            print("Value not found!")

    elif choice == "5":
        print("Inorder Traversal:")
        inorder(root)
        print()

    elif choice == "6":
        print("Preorder Traversal:")
        preorder(root)
        print()

    elif choice == "7":
        print("Postorder Traversal:")
        postorder(root)
        print()

    elif choice == "8":
        print("Program closed.")
        break

    else:
        print("Invalid choice! Please select 1 to 8.")




# 1. LL → Right Rotation
# 2. RR → Left Rotation
# 3. LR → Left + Right Rotation
# 4. RL → Right + Left Rotation

# | Case | Rotation                       |
# | ---- | ------------------------------ |
# | LL   | Right Rotation                 |
# | RR   | Left Rotation                  |
# | LR   | Left Rotation + Right Rotation |
# | RL   | Right Rotation + Left Rotation |


# LL Case

# Insert:

# 30
# 20
# 10

# Tree:

#       30
#      /
#     20
#    /
#   10

# Balance factor of 30:

# +2

# Ye LL case hai.

# Right rotation:

#        20
#       /  \
#     10    30

# Balanced ✅

# 5. RR Case

# Insert:

# 10
# 20
# 30

# Tree:

# 10
#   \
#    20
#      \
#       30

# Ye RR case hai.

# Left rotation:

#        20
#       /  \
#     10    30

# Balanced ✅

# 6. LR Case

# Insert:

# 30
# 10
# 20

# Tree:

#       30
#      /
#     10
#       \
#        20

# Ye LR case hai.

# Pehle 10 par left rotation:

#       30
#      /
#     20
#    /
#   10

# Phir 30 par right rotation:

#        20
#       /  \
#     10    30
# 7. RL Case

# Insert:

# 10
# 30
# 20

# Tree:

# 10
#   \
#    30
#    /
#   20

# Ye RL case hai.

# Pehle 30 par right rotation:

# 10
#   \
#    20
#      \
#       30

# Phir 10 par left rotation:

#        20
#       /  \
#     10    30