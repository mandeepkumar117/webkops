# numbers=int(input("Enter any number: "))
numbers=eval(input("Enter any number: "))
largest=numbers[0]
for num in numbers:
    if num >largest:
        largest=num
print("largest number is: ",largest)