def merge_sort(numbers):

    # Agar list mein 1 ya 0 element hai,
    # to list already sorted hai
    if len(numbers) <= 1:
        return numbers

    # Middle position find karna
    mid = len(numbers) // 2

    # Left half
    left = numbers[:mid]

    # Right half
    right = numbers[mid:]

    # Left half ko recursively sort karna
    left = merge_sort(left)

    # Right half ko recursively sort karna
    right = merge_sort(right)

    # Dono sorted lists ko merge karna
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:

            result.append(left[i])
            i = i + 1

        else:

            result.append(right[j])
            j = j + 1

    # Agar left mein elements bach gaye
    while i < len(left):

        result.append(left[i])
        i = i + 1

    # Agar right mein elements bach gaye
    while j < len(right):

        result.append(right[j])
        j = j + 1

    return result


numbers = [5, 3, 4, 1, 2]

result = merge_sort(numbers)

print("Sorted list:", result)


# 1. Merge Sort kya hai?

# Merge Sort ka main concept hai:

# Divide → Sort → Merge

# Isko Divide and Conquer algorithm bhi kehte hain.

# Suppose:

# [5, 3, 4, 1, 2]

# Pehle list ko chhote parts mein divide karenge:

# [5, 3, 4, 1, 2]
#         ↓
# [5, 3]     [4, 1, 2]
#    ↓           ↓
# [5] [3]     [4] [1, 2]
#                  ↓
#                [1] [2]

# Ab single elements ko merge karte hue sort karenge:

# [5] + [3]
#    ↓
# [3, 5]

# Aur:

# [1] + [2]
#    ↓
# [1, 2]

# Phir:

# [4] + [1, 2]
#        ↓
# [1, 2, 4]

# Finally:

# [3, 5] + [1, 2, 4]
#           ↓
# [1, 2, 3, 4, 5]


# 4. Ab code ko line-by-line samjho
# Step 1
# def merge_sort(numbers):

# Ek function banaya:

# merge_sort()

# Isko list denge aur ye sorted list return karega.

# Step 2 — Base Case
# if len(numbers) <= 1:
#     return numbers

# Ye bahut important hai.

# Agar list:

# [5]

# hai, to isko aur divide karne ki zarurat nahi.

# Single element already sorted hai.

# Example:

# [5] → sorted
# [3] → sorted
# [1] → sorted

# Isi ko base case kehte hain.

# 5. Middle find karna
# mid = len(numbers) // 2

# Example:

# [5, 3, 4, 1, 2]

# Length:

# 5

# So:

# 5 // 2 = 2

# Therefore:

# mid = 2
# 6. List ko divide karna
# left = numbers[:mid]
# right = numbers[mid:]

# Original:

# [5, 3, 4, 1, 2]

# Left:

# [5, 3]

# Right:

# [4, 1, 2]
# 7. Recursion

# Ab:

# left = merge_sort(left)

# Matlab:

# [5,3]

# ko dobara divide karo.

# Aur:

# right = merge_sort(right)

# Matlab:

# [4,1,2]

# ko bhi dobara divide karo.

# 8. Complete Dry Run

# Original:

# [5, 3, 4, 1, 2]
# First division:
#            [5,3,4,1,2]
#              /     \
#           [5,3]   [4,1,2]
# Second division:
#        [5,3]          [4,1,2]
#        /   \           /   \
#      [5]   [3]       [4]  [1,2]
# Third division:
# [1,2]
#  / \
# [1] [2]

# Ab saare parts single elements ho gaye:

# [5]
# [3]
# [4]
# [1]
# [2]

# Ab merge phase start hoga.

# 9. Merge [5] and [3]

# Compare:

# 5 < 3

# ❌

# So 3 pehle:

# [3]

# Phir 5:

# [3,5]
# 10. Merge [1] and [2]

# Compare:

# 1 < 2

# ✅

# Result:

# [1,2]
# 11. Merge [4] and [1,2]

# Ab:

# left  = [4]
# right = [1,2]

# Compare:

# 4 < 1

# ❌

# So 1 result mein:

# [1]

# Ab:

# 4 < 2

# ❌

# So 2:

# [1,2]

# Ab right side khatam.

# Left mein 4 bach gaya:

# [1,2,4]
# 12. Final Merge

# Ab hamare paas:

# left  = [3,5]
# right = [1,2,4]

# Compare one-by-one.

# Comparison 1
# 3 < 1

# ❌

# Take 1:

# [1]
# Comparison 2
# 3 < 2

# ❌

# Take 2:

# [1,2]
# Comparison 3
# 3 < 4

# ✅

# Take 3:

# [1,2,3]
# Comparison 4
# 5 < 4

# ❌

# Take 4:

# [1,2,3,4]

# Ab right side khatam.

# Left mein 5 bacha:

# [1,2,3,4,5]

# 🎉 Final sorted list!