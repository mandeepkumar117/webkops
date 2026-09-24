# numbers = [1, 2, 3, 5, 6]

# n = 6

# for i in range(1, n + 1):
#     if i not in numbers:
#         print("Missing number:", i)
#         break


numbers = [1, 2, 3, 5, 6]

n = 6

expected_sum = 0
actual_sum = 0

for i in range(1, n + 1):
    expected_sum = expected_sum + i

for num in numbers:
    actual_sum = actual_sum + num

missing = expected_sum - actual_sum

print("Missing number:", missing)