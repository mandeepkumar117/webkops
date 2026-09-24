numbers = [1, 2, 3, 4]

result = []

for i in range(len(numbers)):
    multiply = 1

    for j in range(len(numbers)):
        if i != j:
            multiply = multiply * numbers[j]

    result = result + [multiply]

print(result)