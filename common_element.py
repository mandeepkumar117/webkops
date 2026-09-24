list1 = eval(input("Enter first list: "))
list2 = eval(input("Enter second list: "))

result = []

for num in list1:
    if num in list2:
        if num not in result:
            result = result + [num]

print("Common elements:", result)