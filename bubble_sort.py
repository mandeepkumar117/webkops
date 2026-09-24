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