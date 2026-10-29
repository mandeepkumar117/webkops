def heapify(numbers, length, i):

    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < length and numbers[left] > numbers[largest]:
        largest = left

    if right < length and numbers[right] > numbers[largest]:
        largest = right

    if largest != i:

        temp = numbers[i]
        numbers[i] = numbers[largest]
        numbers[largest] = temp

        heapify(numbers, length, largest)


def heap_sort(numbers):

    length = len(numbers)

    # Max Heap banana
    for i in range(length // 2 - 1, -1, -1):
        heapify(numbers, length, i)

    # Largest element ko end mein bhejna
    for i in range(length - 1, 0, -1):

        temp = numbers[0]
        numbers[0] = numbers[i]
        numbers[i] = temp

        heapify(numbers, i, 0)


numbers = [5, 3, 8, 1, 4]

heap_sort(numbers)

print("Sorted list:", numbers)




# 1. Heap Sort kya hai?

# Heap Sort mein hum Heap Data Structure ka use karke sorting karte hain.

# Ascending order ke liye hum generally Max Heap use karte hain.

# Max Heap ka simple meaning:

# Parent node apne children se bada ya equal hota hai.

# Example:

#         9
#        / \
#       7   8
#      / \
#     3   5

# Yahan 9 sabse bada element hai.

# Isliye Max Heap ka root hamesha largest element hota hai.

# 2. Heap Sort ka main idea

# Maan lo:

# [5, 3, 8, 1, 4]

# Heap Sort roughly ye karega:

# Array
#   ↓
# Max Heap banao
#   ↓
# Largest element root par
#   ↓
# Root ko last position se swap
#   ↓
# Heap size chhota karo
#   ↓
# Dobara heapify
#   ↓
# Repeat

# Memory trick:

# Build Heap → Largest ko End mein bhejo → Heapify → Repeat

# 3. Pehle Heap ko samjho

# Array:

# [5, 3, 8, 1, 4]

# Isko tree ki tarah socho:

#         5
#        / \
#       3   8
#      / \
#     1   4

# Indexes:

# index:   0   1   2   3   4
# value:   5   3   8   1   4

# Parent-child relationship:

# index 0 → children 1, 2
# index 1 → children 3, 4

# General formula:

# Left child  = 2*i + 1
# Right child = 2*i + 2
# Parent      = (i - 1) // 2
# 4. Max Heap banana

# Current:

#         5
#        / \
#       3   8
#      / \
#     1   4

# Yahan 5 < 8.

# Max Heap mein parent bada hona chahiye.

# So 5 aur 8 swap:

#         8
#        / \
#       3   5
#      / \
#     1   4

# Array:

# [8, 3, 5, 1, 4]

# Ab 3 ke children:

# 1, 4

# 3 < 4, so swap:

#         8
#        / \
#       4   5
#      / \
#     1   3

# Array:

# [8, 4, 5, 1, 3]

# Ab Max Heap ready:

#         8
#        / \
#       4   5
#      / \
#     1   3

# Largest:

# 8

# root par hai.

# 5. Ab largest ko end mein bhejo

# Current:

# [8, 4, 5, 1, 3]

# Root 8 ko last element 3 se swap:

# [3, 4, 5, 1, 8]

# Ab 8 apni final position par hai.

# Hum ab 8 ko dobara heap mein include nahi karenge.

# Heap portion:

# [3, 4, 5, 1]

# Sorted portion:

# [8]
# 6. Dobara Heapify

# Heap portion:

# [3, 4, 5, 1]

# Tree:

#         3
#        / \
#       4   5
#      /
#     1

# Root 3 hai.

# Children:

# 4 and 5

# Sabse bada:

# 5

# So 3 aur 5 swap:

#         5
#        / \
#       4   3
#      /
#     1

# Array:

# [5, 4, 3, 1, 8]
# 7. Phir largest ko end mein

# Current heap:

# [5, 4, 3, 1]

# Root 5 ko last heap element 1 se swap:

# [1, 4, 3, 5, 8]

# Ab:

# [5, 8] 

# sorted portion hai.

# Heap:

# [1, 4, 3]
# 8. Dobara Heapify
# [1, 4, 3]

# Tree:

#       1
#      / \
#     4   3

# Largest child:

# 4

# Swap:

#       4
#      / \
#     1   3

# Array:

# [4, 1, 3, 5, 8]

# Ab 4 ko end of heap se swap:

# [3, 1, 4, 5, 8]
# 9. Last remaining heap

# Heap:

# [3, 1]

# Tree:

#     3
#    /
#   1

# Already Max Heap hai.

# Swap:

# [1, 3, 4, 5, 8]

# 🎉 Sorted!