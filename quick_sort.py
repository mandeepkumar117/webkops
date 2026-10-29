def quick_sort(numbers):

    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]

    left = []
    right = []

    for i in range(1, len(numbers)):

        if numbers[i] < pivot:
            left.append(numbers[i])

        else:
            right.append(numbers[i])

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right


numbers = [5, 3, 8, 1, 4]

result = quick_sort(numbers)

print("Sorted list:", result)




# 1. Sabse pehle Quick Sort ka main idea

# Quick Sort mein ek element ko hum Pivot banate hain.

# Phir baaki elements ko pivot ke comparison se do groups mein baantte hain:

# Pivot se chhote  → Left
# Pivot            → Beech mein
# Pivot se bade    → Right

# Example:

# [5, 3, 8, 1, 4]

# Hum pehla element 5 pivot lete hain.

# Pivot = 5

# Ab baaki elements check karenge.

# 2. 3 ko check karo
# 3 < 5

# Haan ✅

# To 3 left mein:

# Left = [3]
# 3. 8 ko check karo
# 8 < 5

# Nahi ❌

# To 8 right mein:

# Right = [8]
# 4. 1 ko check karo
# 1 < 5

# Haan ✅

# Left:

# Left = [3, 1]
# 5. 4 ko check karo
# 4 < 5

# Haan ✅

# Left:

# Left = [3, 1, 4]

# Right:

# Right = [8]

# Ab original list:

# [5, 3, 8, 1, 4]

# partition hone ke baad:

# [3, 1, 4]   5   [8]
#     LEFT   PIVOT RIGHT

# Yahi Quick Sort ka partition concept hai.

# 6. Ab kya karna hai?

# Ab humne 5 ko uski correct position ke beech mein rakh diya.

# Lekin:

# [3, 1, 4]

# abhi sorted nahi hai.

# Isliye left part par dobara Quick Sort lagayenge.

# Right:

# [8]

# mein sirf ek element hai, isliye woh already sorted hai.

# 7. Left part par Quick Sort

# Ab:

# [3, 1, 4]

# Pehla element pivot:

# Pivot = 3

# Baaki:

# 1
# 4

# check karenge.

# 1 check
# 1 < 3

# Haan ✅

# Left = [1]
# 4 check
# 4 < 3

# Nahi ❌

# Right = [4]

# To:

# [1]   3   [4]

# Ab 3 bhi apni correct position par hai.

# 8. Ab [1]
# [1]

# Sirf ek element hai.

# Ye already sorted hai.

# So:

# [1]
# 9. Ab [4]
# [4]

# Sirf ek element hai.

# Ye bhi already sorted hai.

# So:

# [4]
# 10. Ab [1] + [3] + [4]

# Combine:

# [1] + [3] + [4]

# Result:

# [1, 3, 4]

# Left part sorted ho gaya.

# 11. Ab original pivot 5 ko yaad karo

# Original partition tha:

# [3, 1, 4]   5   [8]

# Left sort hone ke baad:

# [1, 3, 4]   5   [8]

# Right already sorted:

# [8]

# Combine:

# [1, 3, 4] + [5] + [8]

# Final:

# [1, 3, 4, 5, 8]

# 🎉 Quick Sort complete.