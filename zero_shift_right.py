numbers = [0, 1, 0, 3, 12]

position = 0

for i in range(len(numbers)):
    if numbers[i] != 0:
        temp = numbers[position]
        numbers[position] = numbers[i]
        numbers[i] = temp
        position = position + 1

print(numbers)