# numbers = [10, 20, 30, 40, 50]

# target = 30

# found = False

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         print("Number found at index:", i)
#         found = True
#         break

# if found == False:
#     print("Number not found")

# ===========or===============

numbers=eval(input("Enter list item: "))
length=0
target=eval(input("enter target number: "))
found=False
for num in numbers:
    length=length + 1
for i in range(length):
    if numbers[i]==target:
        print("Number found at index:",i)
        found=True
        break
if found == False:
    print("Number not found")