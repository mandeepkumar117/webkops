numbers = eval(input("Enter list: "))

numbers.sort()

print("Sorted list:", numbers)

target = int(input("Enter number to search: "))

left = 0
right = len(numbers) - 1

while left <= right:

    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Number found at index:", mid)
        break

    elif target > numbers[mid]:
        left = mid + 1

    else:
        right = mid - 1

else:
    print("Number not found")