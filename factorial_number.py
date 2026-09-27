# num = int(input("Enter any number: "))

# if num < 0:
#     print("Factorial is not defined for negative numbers")
# else:
#     fact = 1
#     i = 1

#     print("Factorial of number:", end=" ")

#     while i <= num:
#         print(i, end="")

#         fact = fact * i

#         if i != num:
#             print(" * ", end="")

#         i = i + 1

#     print(" =", fact)


num = int(input("Enter any number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    fact = 1

    print("Factorial of number:", end=" ")

    for i in range(1, num + 1):
        print(i, end="")

        fact = fact * i

        if i != num:
            print(" * ", end="")

    print(" =", fact)