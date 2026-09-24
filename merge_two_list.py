# list1 = eval(input("Enter first list: "))
# list2 = eval(input("Enter second list: "))

# result = []

# for num in list1:
#     result = result + [num]

# for num in list2:
#     result = result + [num]

# print("Merged list:", result)


# remove duplicates

list1 = eval(input("Enter first list: "))
list2 = eval(input("Enter second list: "))

result = []

for num in list1:
    if num not in result:
        result = result + [num]

for num in list2:
    if num not in result:
        result = result + [num]

print("Merged list:", result)