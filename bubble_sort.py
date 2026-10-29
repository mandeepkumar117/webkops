numbers = eval(input("Enter list: "))

length = 0

for num in numbers:
    length = length + 1

for i in range(length):

    for j in range(0, length - i - 1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Sorted list:", numbers)


# 1. Bubble Sort kya karta hai?

# Bubble Sort mein hum adjacent elements yani paas-paas wale elements ko compare karte hain.

# Agar:

# left element > right element

# to dono ko swap kar dete hain.

# Example:

# 5  3

# 5 > 3 hai, isliye swap:

# 3  5

# Har pass ke baad sabse bada element right side mein chala jata hai.

# Isi wajah se ise Bubble Sort kehte hain — bada element dheere-dheere end ki taraf "bubble" karta hai.

# 2. Code

# Aapke preferred style mein, bina sort() aur bina len():

numbers = eval(input("Enter list: "))

# List ki length manually count karna
length = 0

for num in numbers:
    length = length + 1

# Bubble Sort
for i in range(length):

    for j in range(0, length - i - 1):

        if numbers[j] > numbers[j + 1]:

            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Sorted list:", numbers)

# Ab isko ek-ek line samajhte hain.

# 3. Example lete hain

# Input:

# [5, 3, 4, 1, 2]

# Humein ascending order chahiye:

# [1, 2, 3, 4, 5]

# Starting:

# 5  3  4  1  2
# 4. Length count
# length = 0

# for num in numbers:
#     length = length + 1

# List:

# [5, 3, 4, 1, 2]

# Counting:

# num	length
# 5	1
# 3	2
# 4	3
# 1	4
# 2	5

# So:

# length = 5
# 5. Outer loop
# for i in range(length):

# Yani:

# i = 0
# i = 1
# i = 2
# i = 3
# i = 4

# Ye passes control karta hai.

# 6. Inner loop
# for j in range(0, length - i - 1):

# Sabse important line ye hai.

# Starting mein:

# i = 0

# to:

# range(0, 5 - 0 - 1)

# =>

# range(0, 4)

# Therefore:

# j = 0
# j = 1
# j = 2
# j = 3

# Hum adjacent elements compare karenge.

# 7. PASS 1

# Starting list:

# [5, 3, 4, 1, 2]
# Comparison 1

# j = 0

# Compare:

# numbers[0] > numbers[1]

# Means:

# 5 > 3

# Yes ✅

# Swap:

# [3, 5, 4, 1, 2]
# Comparison 2

# j = 1

# Compare:

# 5 > 4

# Yes ✅

# Swap:

# [3, 4, 5, 1, 2]
# Comparison 3

# j = 2

# Compare:

# 5 > 1

# Yes ✅

# Swap:

# [3, 4, 1, 5, 2]
# Comparison 4

# j = 3

# Compare:

# 5 > 2

# Yes ✅

# Swap:

# [3, 4, 1, 2, 5]
# Pass 1 complete:
# [3, 4, 1, 2, 5]

# Notice:

# 5

# sabse right mein aa gaya.

# Largest element apni final position par aa gaya.