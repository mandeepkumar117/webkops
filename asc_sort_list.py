# numbers=eval(input("enter list item: "))
# length=0
# for num in numbers:
#     length=length+1
# for i in range(length):
#     for j in range(i+1,length):
#         if numbers[i]>numbers[j]:
#             temp=numbers[i]
#             numbers[i]=numbers[j]
#             numbers[j]=temp
# print(numbers)


# using one pointer

numbers = eval(input("Enter list item: "))
length = 0
for num in numbers:
    length = length + 1
i = 0
while i < length - 1:
    if numbers[i] > numbers[i + 1]:
        temp = numbers[i]
        numbers[i] = numbers[i + 1]
        numbers[i + 1] = temp
        i = 0
    else:
        i = i + 1

print(numbers)