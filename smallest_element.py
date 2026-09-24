numbers=eval(input("Enput any number: "))
smallest=numbers[0]
for num in numbers:
    if num < smallest:
        smallest=num
print("smallest number is: ",smallest)