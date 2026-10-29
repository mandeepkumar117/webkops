# numbers = [1, 2, 3, 5, 6]

# n = 6

# for i in range(1, n + 1):
#     if i not in numbers:
#         print("Missing number:", i)
#         break


numbers = eval(input("Enter a list of numbers: "))

n = int(input("Enter the maximum number: "))

expected_sum = 0
actual_sum = 0

# 1 se n tak sabhi numbers ka sum
for i in range(1, n + 1):
    expected_sum = expected_sum + i

# List ke numbers ka sum
for num in numbers:
    actual_sum = actual_sum + num

# Missing number find karna
missing = expected_sum - actual_sum

print("Missing number:", missing)