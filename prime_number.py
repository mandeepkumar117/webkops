# n = int(input("enter number: "))
# if n <= 1:
#     print("not a prime")
# else:
#     is_prime = True
#     for i in range(2, n // 2 + 1):
#         if n % i == 0:
#             is_prime = False
#             print(f"divisible by {i}")
#             break
    
#     if is_prime:
#         print("prime")
#     else:
#         print("not a prime")


# count how many prime number in a given range

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0

for n in range(start, end + 1):

    if n <= 1:
        continue

    is_prime = True

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n)
        count = count + 1

print("Total prime numbers:", count)