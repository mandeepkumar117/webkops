numbers = eval(input("Enter list: "))

# Length manually count karna
length = 0

for num in numbers:
    length = length + 1

# Insertion Sort
for i in range(1, length):

    current = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > current:

        numbers[j + 1] = numbers[j]
        j = j - 1

    numbers[j + 1] = current

print("Sorted list:", numbers)


# Step 1: Input

# Maan lo user enter karta hai:

# [5, 3, 4, 1, 2]

# To:

# numbers = [5, 3, 4, 1, 2]
# Step 2: Length count
# length = 0

# Phir:

# for num in numbers:
#     length = length + 1

# List mein 5 elements hain:

# 5 → length = 1
# 3 → length = 2
# 4 → length = 3
# 1 → length = 4
# 2 → length = 5

# Ab:

# length = 5
# Step 3: Main loop
# for i in range(1, length):

# Yahan i 1 se start hota hai.

# i = 1
# i = 2
# i = 3
# i = 4
# i = 0 se kyun nahi?

# Kyuki pehla element:

# [5]

# ko hum already sorted maan lete hain.

# [5] | [3, 4, 1, 2]

# Left side = sorted
# Right side = unsorted

# Step 4: i = 1

# List:

# [5, 3, 4, 1, 2]
#     ↑
#     i

# Ab:

# current = numbers[i]

# Matlab:

# current = numbers[1]
# current = 3

# Ab:

# current = 3
# Step 5: j = i - 1
# j = i - 1

# i = 1 hai:

# j = 1 - 1
# j = 0

# Matlab j current element ke just left wale element par hai.

# [5, 3, 4, 1, 2]
#  ↑  ↑
#  j  i
# Step 6: While condition
# while j >= 0 and numbers[j] > current:

# Check:

# j >= 0
# 0 >= 0 → True

# Aur:

# numbers[j] > current
# numbers[0] > 3
# 5 > 3 → True

# Dono True hain.

# Step 7: Shift
# numbers[j + 1] = numbers[j]

# Ab:

# numbers[1] = numbers[0]

# Matlab:

# 3 ki jagah 5

# List:

# [5, 5, 4, 1, 2]

# Phir:

# j = j - 1
# j = 0 - 1
# j = -1
# Step 8: While ruk gaya

# Ab:

# j >= 0
# -1 >= 0 → False

# To while loop stop.

# Ab:

# numbers[j + 1] = current

# j = -1

# Isliye:

# j + 1 = 0

# So:

# numbers[0] = 3

# List:

# [3, 5, 4, 1, 2]
# First pass complete ✅
# [3, 5] | [4, 1, 2]