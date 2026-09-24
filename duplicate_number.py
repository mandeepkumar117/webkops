numbers=eval(input("Enter a list item number: "))
length=0
for num in numbers:
    length=length + 1
for i in range(length):
    for j in range(i+1,length):
        if numbers[i]==numbers[j]:
            print(numbers[i])
            break

# built in method

# numbers = [10, 20, 30, 20, 40, 10]

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):

#         if numbers[i] == numbers[j]:
#             print("D  uplicate:", numbers[i])
#             break