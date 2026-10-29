
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert operation
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

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


# Minimum value find karna
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

        # Dono children hain
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


# Update operation
def update(root, old_value, new_value):
    if not search(root, old_value):
        print("Old value not found!")
        return root

    if search(root, new_value):
        print("New value already exists!")
        return root

    root = delete(root, old_value)
    root = insert(root, new_value)

    print("Value updated successfully!")
    return root

# Preorder: Root -> Left -> Right
def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

# Inorder traversal
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

# Initial BST
n = int(input("Enter number of nodes: "))
root = None

for i in range(n):
    value = int(input("Enter value: "))
    root = insert(root, value)


# Menu
while True:
    print("\n\n--- BST MENU ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    print("4. Search")
    print("5. Display")
    print("6. Preorder")
    print("7. Postorder")    
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
        print("Invalid choice!")
