# numbers=eval(input("Enter a list item: "))
# target=eval(input("Enter target value"))
# length=0
# for num in numbers:
#     length=length + 1
# for i in range(length):
#     for j in range(i+1,length):
#         if numbers[i] + numbers[j]==target:
#             print(i,j)

# built in method

numbers = [2, 7, 11, 15]
target = 9

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print([i, j])