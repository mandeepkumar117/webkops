numbers = eval(input("Enter list: "))

length = 0

for num in numbers:
    length = length + 1

for i in range(length):

    smallest = i

    for j in range(i + 1, length):

        if numbers[j] < numbers[smallest]:
            smallest = j

    temp = numbers[i]
    numbers[i] = numbers[smallest]
    numbers[smallest] = temp

print("Sorted list:", numbers)



# 1. Selection Sort kya karta hai?

# Selection Sort ka simple idea hai:

# Unsorted part mein se sabse chhota element dhoondo → current position par le aao.

# Example:

# [5, 3, 4, 1, 2]

# Pehle poori list mein smallest dhoondenge:

# 1

# Phir 1 ko first position par rakhenge:

# [1, 3, 4, 5, 2]

# Phir remaining part:

# [3, 4, 5, 2]

# mein smallest 2 hai.

# Usko second position par rakhenge:

# [1, 2, 4, 5, 3]

# Aise hi karte-karte list sort ho jayegi.

# 2. Code

# Aapke preferred style mein:

# numbers = eval(input("Enter list: "))

# # List ki length manually count karna
# length = 0

# for num in numbers:
#     length = length + 1

# # Selection Sort
# for i in range(length):

#     # Maan lo current position ka element hi smallest hai
#     smallest = i

#     # Baaki unsorted elements mein smallest dhoondna
#     for j in range(i + 1, length):

#         if numbers[j] < numbers[smallest]:
#             smallest = j

#     # Smallest element ko current position par lana
#     temp = numbers[i]
#     numbers[i] = numbers[smallest]
#     numbers[smallest] = temp

# print("Sorted list:", numbers)
# 3. Example

# Hum ye list lenge:

# [5, 3, 4, 1, 2]

# Expected output:

# [1, 2, 3, 4, 5]
# 4. Length count
# length = 0

# for num in numbers:
#     length = length + 1

# List mein 5 elements hain:

# 5
# 3
# 4
# 1
# 2

# Isliye:

# length = 5
# 5. Outer loop
# for i in range(length):

# Yani:

# i = 0
# i = 1
# i = 2
# i = 3
# i = 4

# i batata hai:

# Abhi kis position par smallest element rakhna hai?

# 6. Sabse important line
# smallest = i

# Iska matlab:

# Abhi temporarily maan lo ki i position wala element hi smallest hai.

# Example:

# [5, 3, 4, 1, 2]
#  ↑
#  i = 0

# To:

# smallest = 0

# Yani abhi hum maan rahe hain:

# 5 smallest hai

# Lekin ye sirf assumption hai. Ab hum baaki elements check karenge.

# 7. Inner loop
# for j in range(i + 1, length):

# Agar:

# i = 0

# to:

# j = 1, 2, 3, 4

# Hum 5 ko khud se compare nahi karenge.

# Uske baad ke elements check karenge:

# 3
# 4
# 1
# 2
# 8. Pass 1 — complete dry run

# Starting:

# [5, 3, 4, 1, 2]
# Step 1
# i = 0
# smallest = 0

# Ab:

# numbers[smallest] = 5

# So currently:

# smallest = 5
# Step 2

# j = 1

# Compare:

# numbers[j] < numbers[smallest]

# Means:

# 3 < 5

# Yes ✅

# To:

# smallest = 1

# Ab smallest:

# 3
# Step 3

# j = 2

# Compare:

# 4 < 3

# ❌ No.

# So:

# smallest = 1

# still.

# Step 4

# j = 3

# Compare:

# 1 < 3

# Yes ✅

# So:

# smallest = 3

# Ab smallest:

# 1
# Step 5

# j = 4

# Compare:

# 2 < 1

# ❌ No.

# So final:

# smallest = 3

# Matlab smallest element hai:

# 1

# Aur 1 index 3 par hai.

# 9. Ab swap

# Code:

# temp = numbers[i]
# numbers[i] = numbers[smallest]
# numbers[smallest] = temp

# Current list:

# [5, 3, 4, 1, 2]

# i = 0

# smallest = 3

# Pehle:

# temp = numbers[i]

# So:

# temp = 5

# Then:

# numbers[i] = numbers[smallest]

# Yani:

# numbers[0] = numbers[3]

# List:

# [1, 3, 4, 1, 2]

# Ab:

# numbers[smallest] = temp

# Yani:

# numbers[3] = 5

# Final:

# [1, 3, 4, 5, 2]
# Pass 1 complete:
# [1, 3, 4, 5, 2]
#  ↑
# fixed

# 1 apni final position par aa gaya.