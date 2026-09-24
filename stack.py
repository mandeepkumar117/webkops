stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Pop
item = stack.pop()
print("Removed:", item)

print("Stack after pop:", stack)

# Top element
print("Top element:", stack[-1])