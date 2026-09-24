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